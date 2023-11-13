# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models

# Snippets --> omod -->

#class PracticaLiberia(models.Model):
#    _name = "practica_libreria"
#    _description = "Modelo para registrar libros"

class PracticaLBookstore(models.Model):
    _name = "practica.bookstore"
    _description = "Template for registering books"

    # Nombre del libro - Carácteres
    # Como el título y el nombre son iguales prodríamos ponerlo de la siguiente forma también:
    # name = fields.Char()
    # Odoo ya lo pone de forma automática con una mayúscula al inicio
    name = fields.Char(string='Book Name')

    # Precio - Números decimales
    # price = fields.Float()
    price = fields.Float(string='Price')
    
    # Edición - Números enteros
    # edition = fields.Float()
    edition = fields.Integer(string='Edition')

    # Formato - Selector
    format = fields.Selection(string='Format', selection=[('printed', 'Printed'), ('digital', 'Digital')])

    # Enlace web de compra - Carácteres
    # link = fields.Float()
    link = fields.Char(string='Link')

    # Se ha comprado - Números enteros
    buy = fields.Boolean(string='Purchased?')

    # Fecha de compra - Fecha
    date = fields.Date(string='Date of purchase')

    # Usuario - Carácteres
    # Como extra hemos referenciado a otra tabla como es la de "res.partner" para enlazar cada artículo con un usuario
    adress_id = fields.Many2one(string='User',
        comodel_name='res.partner',
        ondelete='restrict')
