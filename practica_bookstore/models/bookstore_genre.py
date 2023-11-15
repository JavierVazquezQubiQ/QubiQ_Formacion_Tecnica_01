# Copyright 2023 - Javier Vázquez Flores

# Importa las clases fields y models del módulo "odoo".
from odoo import fields, models, fields

# Define una nueva clase llamada "BookstoreGenre" que hereda de "models.Model". Representa el modelo de datos para géneros de libros en Odoo.
class BookstoreGenre(models.Model):  
    # Establece el nombre técnico y una descripción del modelo.
    _name = "bookstore.genre"
    _description = "Template for genre registration"
    
    # Define un campo llamado "name" de tipo Char (texto) en el modelo.
    name = fields.Char(string='Genre', required=True)  # Define un campo "genre" de tipo Char (texto) en el modelo.
    
    # Relaciona este modelo con el modelo "bookstore"
    # Este campo podria servir para que en el futuro se creara un boton dentro del genero que llevará los libros asociados.
    books_ids = fields.Many2many(
    comodel_name='bookstore',
    string='Books',
    ondelete='restrict',
    required=False
    )
    
#     # OPCIÓN 2
    
#     En Odoo, la variable _rec_name se utiliza para especificar el campo que se debe usar para mostrar el nombre de un registro en un modelo.
#     Por defecto, Odoo utiliza el campo name como el campo de representación del registro. Sin embargo, si tu modelo no tiene un campo name o si deseas usar un campo diferente 
#     para representar el nombre del registro, puedes utilizar _rec_name.

# class MiModelo(models.Model):
#     _name = 'mi.modelo'
#     _rec_name = 'mi_campo_nombre'
    
#     mi_campo_nombre = fields.Char(string='Nombre Alternativo')
    
#     # OPCIÓN 3
    
#     genre = fields.Char(string='Genre', required=True)  # Define un campo "genre" de tipo Char (texto) en el modelo.

#     # Definir el método para mostrar el nombre del registro
#     def name_get(self):  # Define un método personalizado llamado "name_get".
#         result = []  # Crea una lista vacía llamada "result" para almacenar los nombres de los registros.
#         for record in self:  # Inicia un bucle "for" que recorre todos los registros del modelo "BookstoreGenre".
#             result.append((record.id, record.genre))  # Agrega una tupla al "result" con el ID del registro y el valor del campo "genre".
#         return result  # Devuelve la lista "result", que contiene las tuplas que representan los nombres de los registros.
    
#     # El método name_get se modifica cuando queremos modifciar el valor del campo que queremos mostrar, como por ejemplo unir la referencia de un libro - nombre del libro.
    
