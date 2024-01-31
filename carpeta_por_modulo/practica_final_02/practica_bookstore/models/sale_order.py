# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import models, exceptions, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            if not order.partner_id.bookstore_partner:
                raise exceptions.UserError(_("You can only sell to members."))
        return super().action_confirm()
