# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models  # Importa las clases fields y models del módulo "odoo".

class BookstorePacks(models.Model):  # Define una nueva clase llamada "BookstoreGenre" que hereda de "models.Model". Representa el modelo de datos para géneros de libros en Odoo.
    _name = "bookstore.packs"  # Establece el nombre técnico del modelo como "bookstore.genre".
    _description = "Template for packing books"  # Proporciona una descripción para el modelo.

    packs = fields.Char(string='Packs', required=True)  # Define un campo "genre" de tipo Char (texto) en el modelo.

    # Definir el método para mostrar el nombre del registro
    def name_get(self):  # Define un método personalizado llamado "name_get".
        result = []  # Crea una lista vacía llamada "result" para almacenar los nombres de los registros.
        for record in self:  # Inicia un bucle "for" que recorre todos los registros del modelo "BookstoreGenre".
            result.append((record.id, record.packs))  # Agrega una tupla al "result" con el ID del registro y el valor del campo "genre".
        return result  # Devuelve la lista "result", que contiene las tuplas que representan los nombres de los registros.
    
    books_ids = fields.Many2many(
    comodel_name='bookstore',
    string='Books',
    ondelete='restrict',
    required=False
    )