# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api


class ProductPackLine(models.Model):
    _name = 'product.pack.line'

    pack_id = fields.Many2one(
        comodel_name='product.product',
        string="Pack",
    )
    component_id = fields.Many2one(
        comodel_name='product.product',
        string="Component",
        required=True,
    )
    quantity = fields.Integer(
        string="Quantity",
        default=1
    )
    price = fields.Float(
        string="Price",
    )

    @api.onchange('component_id')
    def onchange_component_id(self):
        self.price = self.component_id.list_price
