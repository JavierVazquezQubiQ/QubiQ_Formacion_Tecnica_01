# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(
        compute='_compute_name',
        store=True
    )
    first_name = fields.Char()
    last_name = fields.Char()
    book_author = fields.Boolean()
    bookstore_partner = fields.Boolean()
    bookstore_partner_number = fields.Integer(
        string=_('Partner ID')
    )
    author_genre_ids = fields.Many2many(
        comodel_name='bookstore.genre',
        string=_('Genre'),
        ondelete='restrict',
        required=False,
    )

    @api.onchange('first_name', 'last_name')
    def _compute_name(self):
        for record in self:
            if record.first_name and record.last_name:
                record.name = f"{record.first_name} {record.last_name}"
            elif record.first_name:
                record.name = record.first_name
            elif record.last_name:
                record.name = record.last_name
            else:
                record.name = ""

    @api.constrains('book_author')
    def _check_is_author(self):
        for record in self:
            has_book = self.env['bookstore'].search([
                ('author_id', '=', record.id)
                ]
            )
            if has_book and not record.book_author:
                raise ValidationError(_(
                    """
                    You cannot deactivate the author check on a contact with
                    assigned books in the bookstore. Remove them first.
                    """
                ))
