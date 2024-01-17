# Copyright 2023 - Javier Vázquez Flores

from odoo import models, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            if not order.partner_id.bookstore_partner:
                raise exceptions.UserError("You can only sell to members.")
        return super().action_confirm()
