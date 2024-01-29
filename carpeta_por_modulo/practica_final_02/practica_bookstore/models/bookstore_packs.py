# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class BookstorePacks(models.Model):
    _name = "bookstore.packs"
    _description = "Template for packing books"

    name = fields.Selection(
        string='Pack Type',
        selection=[
            ('sagas', 'Sagas'),
            ('colecciones', 'Colecciones')
            ],
        default='colecciones',
        )

    book_ids = fields.Many2many(
        comodel_name='bookstore',
        ondelete='restrict',
        required=False)

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing_record = self.env['bookstore.packs'].search(
                [('name', '=', record.name)]
            )
            if len(existing_record) > 1 or (len(existing_record) == 1 and existing_record != record):
                raise ValidationError(
                    "A pack with the same name already exists!"
                )
