# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class BookstoreGenre(models.Model):
    _name = "bookstore.genre"
    _description = _("Template for genre registration")

    name = fields.Char(
        string=_('Genre'),
        required=True,
        index=True,
        unique=True
    )
    books_ids = fields.Many2many(
        comodel_name='bookstore',
        string=_('Books'),
        ondelete='restrict',
        required=False
    )

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing_record = self.env['bookstore.genre'].search([
                ('name', '=', record.name)]
            )
            if len(existing_record) > 1 or (
                len(existing_record) == 1 and existing_record != record
            ):
                raise ValidationError(_(
                    "A genre with the same name already exists!"
                ))
