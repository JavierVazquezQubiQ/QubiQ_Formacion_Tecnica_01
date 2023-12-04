# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api


class Bookstore(models.Model):
    _name = "bookstore"
    _description = "Template for registering books"
    _inherits = {'product.template': 'product_tmpl_id'}

    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string='Product Template')

    format = fields.Selection(
        string='Format',
        required=True,
        selection=[
            ('printed', 'Printed'),
            ('digital', 'Digital'),
            ],
        )

    edition = fields.Integer(string='Edition', required=False)

    author_id = fields.Many2one(
        string='Book author',
        comodel_name='res.partner',
        domain=[('book_author', '=', True)],
        default=True,
        ondelete='restrict')

    genre_ids = fields.Many2many(
        comodel_name='bookstore.genre',
        string='Genre',
        ondelete='restrict',
        required=False)

    link = fields.Char(string='Link', required=False)

    buy = fields.Boolean(string='Purchased?', required=False)

    date = fields.Date(string='Date of purchase', required=False)

    price = fields.Float(string='Price', required=False)

    pack_check = fields.Boolean(string='Pack?', required=False)

    pack_ids = fields.Many2many(
        comodel_name='bookstore.packs',
        string='Tipo de pack',
        ondelete='restrict',
        required=False,
        )

    @api.onchange('pack_check')
    def _onchange_pack_check(self):
        if self.pack_check:
            pack_type = self.env['bookstore.packs'].search([('name', '=', 'colecciones')], limit=1)
            if pack_type:
                self.pack_ids = [(4, pack_type.id)]
            else:
                # Crea un nuevo registro 'colecciones' en 'bookstore.packs' si no existe
                new_pack = self.env['bookstore.packs'].create({'name': 'colecciones'})
                self.pack_ids = [(4, new_pack.id)]
        else:
            self.pack_ids = [(5, 0, 0)]  # Elimina todos los registros en 'pack_ids'

    '''
    Esta línea es un decorador @api.onchange que indica que la función
    '_onchange_author_id' se ejecutará cada vez que cambie el campo author_id
    en el modelo Bookstore.
    '''

    # Activador: se ejecuta cuando cambia el campo 'author_id'
    @api.onchange('author_id')
    # Define la función _onchange_author_id que toma self como parámetro,
    # significa que opera en instancias individuales del modelo Bookstore.
    def _onchange_author_id(self):
        if self.author_id:  # Verifica si hay un autor seleccionado en el libro
            # Si hay un autor seleccionado, asigna los géneros del autor al
            # campo 'genre_ids' del libro.
            self.genre_ids = [(
                6,
                0,
                self.author_id.author_genre_ids.ids
                if self.author_id.author_genre_ids else []
            )]

            '''
            La estructura (6, 0, [IDs]) se utiliza para indicar que se deben
            reemplazar todos los registros existentes en el campo Many2many
            con los registros especificados por los IDs proporcionados. En
            este contexto:

            6: Es el código para "reemplazar". Indica que se reemplazarán los
            registros existentes en el campo con los nuevos registros
            especificados.

            0: Es el código para "eliminar y agregar". Indica que se deben
            eliminar todos los registros existentes y agregar los nuevos.

            self.author_id.author_genre_ids.ids
            if self.author_id.author_genre_ids else []:
            Es una expresión condicional que proporciona los IDs de los
            géneros asociados al autor (self.author_id).
            Si el autor tiene géneros asociados, utiliza esos IDs; de lo
            contrario, proporciona una lista vacía.
            '''

        else:
            # Si no hay autor seleccionado, elimina los géneros del libro.
            self.genre_ids = False

    @api.model
    def create(self, vals):
        # Crea un product.template
        new_template = super().create(vals)

        # Chequea si dicho libro está guardado como 'consu', en ese caso lo cambia a storable ('product').
        if new_template.detailed_type == 'consu':
            new_template.write({'detailed_type': 'product'})

        return new_template
