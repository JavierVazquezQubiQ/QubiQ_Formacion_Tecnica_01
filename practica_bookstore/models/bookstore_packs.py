# Copyright 2023 - Javier Vázquez Flores

# Importa las clases fields y models del módulo "odoo".
from odoo import fields, models

# Define una nueva clase llamada "BookstoreGenre" que hereda de "models.Model". Representa el modelo de datos para géneros de libros en Odoo.
class BookstorePacks(models.Model):
    # Establece el nombre técnico y una descripción del modelo.
    _name = "bookstore.packs"
    _description = "Template for packing books"  

    # Define un campo llamado "name" de tipo Char (texto) en el modelo.
    name = fields.Char(string='Packs', required=True)  
    
    # Relaciona este modelo con el modelo "bookstore"
    book_id = fields.Many2many(
    comodel_name='bookstore',
    string='Books',
    ondelete='restrict',
    required=False
    )
    
    # component_id = relacion al libro que actuara como componente
    
    # quantity = entero con el numero de libros de compontente
    
    # pack_id = 