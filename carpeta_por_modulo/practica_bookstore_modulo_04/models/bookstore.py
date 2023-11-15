# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api

# Snippets --> omod -->

# EJEMPLO:
#class PracticaLiberia(models.Model):
#    _name = "practica.liberia"
#    _description = "Modelo para registrar libros"

class Bookstore(models.Model):
    _name = "bookstore"
    _description = "Template for registering books"
    _inherits = {'product.template': 'product_tmpl_id'}

    # Relacionamos campo con el modelo product.template
    product_tmpl_id = fields.Many2one(
    comodel_name='product.template', 
    string='Product Template')

    # En este caso no hace falta que añadamos este campo porque lo heredamos directamente del modelo product.template
    # # Nombre del libro - Carácteres.
    # # Como el título y el nombre son iguales prodríamos ponerlo de la siguiente forma también:
    # # name = fields.Char()
    # # Odoo ya lo pone de forma automática con una mayúscula al inicio.
    # name = fields.Char(string='Book Name', required=True)
  
    # Edición - Números enteros.
    # edition = fields.Float()
    edition = fields.Integer(string='Edition', required=False)
    
    # Género - Números enteros.
    # genre_id = fields.Many2one() = Muchos de muchos, te da a elegir entre varias opciones...
    genre_ids = fields.Many2many(
        comodel_name='bookstore.genre',
        string='Genre',
        ondelete='restrict',
        required=False)
    
    # Se ha comprado - Números enteros.
    pack_check = fields.Boolean(string='Pack?', required=False)
    
    # Packs = fields.One2many() = Uno a muchos...
    pack_ids = fields.One2many(
        comodel_name='bookstore.packs',
        inverse_name='book_id',
        string='Packs',
        ondelete='restrict',
        required=False)

    # Formato - Selector.
    format = fields.Selection(string='Format', selection=[('printed', 'Printed'), ('digital', 'Digital')], required=True)

    # Enlace web de compra - Carácteres.
    # link = fields.Float()
    link = fields.Char(string='Link', required=False)

    # Se ha comprado - Números enteros.
    buy = fields.Boolean(string='Purchased?', required=False)

    # Fecha de compra - Fecha.
    date = fields.Date(string='Date of purchase', required=False)
    
    # Precio - Números decimales.
    # price = fields.Float()
    price = fields.Float(string='Price', required=False)

    # Usuario - Carácteres.
    # Como extra hemos referenciado a otra tabla como es la de "res.partner" para enlazar cada artículo con un usuario.
    author_id = fields.Many2one(
        string='Book author',
        comodel_name='res.partner',
        domain=[('book_author', '=', True)],
        default=True,
        ondelete='restrict')