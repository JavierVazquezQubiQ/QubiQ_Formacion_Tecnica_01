# Copyright 2023 - Javier Vázquez Flores

from odoo import models, api, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Verifica si el cliente no es un miembro de la librería
        for order in self:
            if not order.partner_id.bookstore_partner:
                raise exceptions.UserError("You can only sell to members.")

        # Llama al método original de la clase padre
        return super().action_confirm()
