# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commission_line_ids = fields.One2many(
        String=_("Commission Lines"),
        comodel_name='sale.commission',
        inverse_name='sale_id'
    )
