# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Bookstore(models.Model):
    _name = "bookstore"
    _description = _("Template for registering books")
    _inherits = {'product.template': 'product_tmpl_id'}

    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string=_('Product Template')
    )
    format = fields.Selection(
        required=True,
        selection=[
            ('printed', _('Printed')),
            ('digital', _('Digital')),
        ],
    )
    edition = fields.Integer()
    author_id = fields.Many2one(
        string=_('Book author'),
        comodel_name='res.partner',
        domain=[('book_author', '=', True)],
        default=True,
        ondelete='restrict'
    )
    genre_ids = fields.Many2many(
        comodel_name='bookstore.genre',
        ondelete='restrict',
    )
    link = fields.Char()
    buy = fields.Boolean(
        string=_('Purchased?'),
    )
    date = fields.Date(
        string=_('Date of purchase'),
        required=False
    )
    price = fields.Float()
    pack_check = fields.Boolean(
        string=_('Pack?')
    )
    pack_ids = fields.Many2many(
        comodel_name='bookstore.packs',
        string=_('Pack type'),
        ondelete='restrict',
        required=False,
    )
    synopsis = fields.Html(
        help=_("Enter the synopsis of the book"),
    )

    @api.onchange('pack_check')
    def _onchange_pack_check(self):
        """
        Function called when the value of the field 'pack_check' changes.

        This function is triggered by the 'onchange' decorator and is
        responsible for updating the 'pack_ids' field based on the value
        of 'pack_check'.
        """
        if self.pack_check:
            pack_type = self.env['bookstore.packs'].search(
                [('name', '=', 'collections')], limit=1
            )
            if pack_type:
                self.pack_ids = [(4, pack_type.id)]
            else:
                # Create 'Collections'/'Sagas' in 'bookstore.packs' if it doesn't exist
                new_pack_collections = self.env['bookstore.packs'].create(
                    {
                        'name': 'Collections',
                    }
                )
                new_pack_sagas = self.env['bookstore.packs'].create(
                    {
                        'name': 'Sagas',
                    }
                )
                self.pack_ids = [(4, new_pack_collections.id)]
        else:
            self.pack_ids = [(5, 0, 0)]  # Deletes records in 'pack_ids'.

    @api.onchange('author_id')
    def _onchange_author_id(self):
        self.genre_ids = self.author_id.author_genre_ids

    @api.model
    def create(self, vals):
        vals.update({'detailed_type': 'product'})
        new_template = super().create(vals)
        audit_logs = []
        for book in new_template:
            audit_logs.append({
                'action_type': 'create',
                'date_time': fields.Datetime.now(),
                'user_id': self.env.user.id,
                'book_id': book.id,
                'book_name': book.product_tmpl_id.name
            })
        self.env['bookstore.audit'].create(audit_logs)
        return new_template

    def write(self, vals):
        res = super().write(vals)
        for book in self:
            self.env['bookstore.audit'].create({
                'action_type': 'write',
                'date_time': fields.Datetime.now(),
                'user_id': self.env.user.id,
                'book_id': book.id,
                'book_name': book.product_tmpl_id.name
            })
        return res

    def unlink(self):
        audit_logs = []
        for book in self:
            audit_logs.append({
                'action_type': 'unlink',
                'date_time': fields.Datetime.now(),
                'user_id': self.env.user.id,
                'book_id': book.id,
                'book_name': book.product_tmpl_id.name
            })
        self.env['bookstore.audit'].create(audit_logs)
        return super(Bookstore, self).unlink()

    @api.constrains('price')
    def _check_negative_price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError(_(
                    "It is not possible to create negative pricing"
                ))
