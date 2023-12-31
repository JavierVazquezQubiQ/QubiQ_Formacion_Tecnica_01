# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models

# Snippets --> omod -->

#class PracticaLiberia(models.Model):
#    _name = "bookstore"
#    _description = "Modelo para registrar libros"

class Bookstore(models.Model):
    _name = "bookstore"
    _description = "Template for registering books"

    # Nombre del libro - Carácteres.
    # Como el título y el nombre son iguales prodríamos ponerlo de la siguiente forma también:
    # name = fields.Char()
    # Odoo ya lo pone de forma automática con una mayúscula al inicio.
    name = fields.Char(string='Book Name', required=True)
  
    # Edición - Números enteros.
    # edition = fields.Float()
    edition = fields.Integer(string='Edition', required=False)
    
    # Género - Números enteros.
    # genre_id = fields.Many2one() = Uno de muchos, te da a elegir entre varias opciones..
    genre_ids = fields.Many2many(
        comodel_name='bookstore.genre',
        string='Genre',
        ondelete='restrict',
        required=False
        )

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