# Copyright 2023 - Javier Vázquez Flores

# Importa las clases fields y models del módulo "odoo".

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class BookstoreGenre(models.Model):  
    _name = "bookstore.genre"
    _description = "Template for genre registration"

    name = fields.Char(string='Genre', required=True, index=True, unique=True)

    books_ids = fields.Many2many(
        comodel_name='bookstore',
        string='Books',
        ondelete='restrict',
        required=False)

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing_record = self.env['bookstore.genre'].search([('name', '=', record.name)])
            if len(existing_record) > 1 or (len(existing_record) == 1 and existing_record != record):
                raise ValidationError("A genre with the same name already exists!")
