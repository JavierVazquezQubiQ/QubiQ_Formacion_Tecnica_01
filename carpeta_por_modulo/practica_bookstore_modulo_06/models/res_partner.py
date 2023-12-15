# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(compute='_compute_name', store=True)

    bookstore_partner = fields.Boolean(string='Bookstore partner')

    bookstore_partner_number = fields.Integer(string='Partner ID')

    first_name = fields.Char(string='First name')

    last_name = fields.Char(string='Last name')

    book_author = fields.Boolean(string='Book author')

    author_genre_ids = fields.Many2many(
        comodel_name='bookstore.genre',
        string='Genre',
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
            has_book = self.env['bookstore'].search([('author_id', '=', record.id)])
            if has_book and not record.book_author:
                raise ValidationError("You cannot deactivate the author check on a contact with assigned books in the bookstore. Remove them first.")

    # TODO NO FUNCIONA (Para nota)
    # @api.model
    # def write(self, vals):
    #     records = super().write(vals)
    #     for record in records:
    #         has_book = self.env['bookstore'].search([('author_id', '=', record.id)])
    #         if has_book:
    #             record.book_author = True
    #     return records
