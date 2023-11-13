# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models

# Snippets --> omodi

class Contacts(models.Model):
    _inherit = 'res.partner'
    
    library_partner = fields.Boolean(string='Library partner')
    
    library_partner_number = fields.Integer(string='Partner ID')
    
    book_author = fields.Boolean(string='Book author')
