# Copyright 2023 - Javier Vázquez Flores

from odoo import api, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):

        if self.product_id and self.product_id.is_pack and \
           self.product_id.component_line_ids:
            self.name += _('\n-- Components --')

            for line in self.product_id.component_line_ids:
                self.name += '\n %s - %i' % (
                    line.component_id.name,
                    line.quantity,
                )
