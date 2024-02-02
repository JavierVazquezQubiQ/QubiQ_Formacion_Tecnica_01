# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class BookstorePacks(models.Model):
    _name = "bookstore.packs"
    _description = _("Template for packing books")

    name = fields.Selection(
        string='Pack Type',
        selection=[
            ('sagas', _('Sagas')),
            ('collections', _('Collections'))
        ],
        default='collections',
    )
    book_ids = fields.Many2many(
        comodel_name='bookstore',
        string=_('Book IDs'),
        ondelete='restrict',
        required=False
    )

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing_record = self.env['bookstore.packs'].search(
                [('name', '=', record.name)]
            )
            if len(existing_record) > 1 or (
                len(existing_record) == 1 and existing_record != record
            ):
                raise ValidationError(_(
                    "A pack with the same name already exists!"
                ))
