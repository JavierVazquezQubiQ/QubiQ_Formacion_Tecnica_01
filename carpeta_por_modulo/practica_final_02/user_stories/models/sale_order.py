# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commission_line_ids = fields.One2many(
        String="Commission Lines",
        comodel_name='sale.commission',
        inverse_name='sale_id'
    )
