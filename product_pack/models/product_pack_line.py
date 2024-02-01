# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models, api, _


class ProductPackLine(models.Model):
    _name = 'product.pack.line'

    pack_id = fields.Many2one(
        comodel_name='product.template',
        string=_("Pack"),
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string=_("Component"),
        required=True,
    )
    quantity = fields.Integer(
        default=1
    )
    price = fields.Float()

    @api.onchange('quantity', 'product_id')
    def _onchange_price(self):
        for rec in self:
            rec.price = rec.product_id.list_price * rec.quantity
