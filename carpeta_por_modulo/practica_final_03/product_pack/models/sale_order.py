# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import api, models, fields, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    has_pack = fields.Boolean()
    pack_id = fields.Many2one(
        comodel_name='product.template',
        string=_('Pack'),
        domain=[
            ('is_pack', '=', True),
        ],
    )

    @api.onchange('pack_id')
    def on_change_pack_id(self):
        """
        This function adds the selected pack and its components to the
        sales order. Delete old sales lines and create new ones for the
        selected pack.
        """
        if self.pack_id:
            self.order_line = False

            # Add the product
            self.env['sale.order.line'].new({
                'product_id': self.pack_id.id,
                'order_id': self.id,
                'product_uom_qty': 1,
            })

            # Add the components of the package for that product
            for component_line in self.pack_id.component_line_ids:
                self.env['sale.order.line'].new({
                    'product_id': component_line.product_id.id,
                    'order_id': self.id,
                    'product_uom_qty': component_line.quantity or 1,
                })
