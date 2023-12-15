# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api
from odoo.exceptions import ValidationError


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
        # inverse_name='book_ids',
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
                # Crea un nuevo registro 'Colecciones' / 'Sagas' en 'bookstore.packs' si no existe
                new_pack_colecciones = self.env['bookstore.packs'].create({'name': 'Colecciones'})
                new_pack_sagas = self.env['bookstore.packs'].create({'name': 'Sagas'})
                self.pack_ids = [(4, new_pack_colecciones.id)]
        else:
            self.pack_ids = [(5, 0, 0)]  # Elimina todos los registros en 'pack_ids'

    @api.onchange('author_id')
    def _onchange_author_id(self):
        self.genre_ids = self.author_id.author_genre_ids

    def create(self, vals):
        new_template = super().create(vals)
        if new_template.detailed_type == 'consu':
            new_template.write({'detailed_type': 'product'})
        return new_template
