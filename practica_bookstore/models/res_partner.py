# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models

# Snippets --> omodi

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    bookstore_partner = fields.Boolean(string='Bookstore partner')
    
    bookstore_partner_number = fields.Integer(string='Partner ID')
    
    book_author = fields.Boolean(string='Book author')

    author_genre_ids = fields.Many2many(
        comodel_name='bookstore.genre',
        string='Genre',
        ondelete='restrict',
        required=False)