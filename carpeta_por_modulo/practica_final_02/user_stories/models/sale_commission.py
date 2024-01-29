# Copyright 2023 - Javier Vázquez Flores

from odoo import api, fields, models


class SaleCommission(models.Model):
    _name = 'sale.commission'
    _description = 'Sale Commission'

    name = fields.Many2one(
        string='Commercial',
        comodel_name="res.partner",
        domain="[('is_commercial', '=', True)]"
    )
    commission = fields.Float(
        string='%'
    )
    sale_id = fields.Many2one(
        comodel_name='sale.order'
    )
    amount = fields.Float(
        compute='_compute_amount',
        store=True
    )

    @api.onchange('name')
    def onchange_name(self):
        self.commission = self.name.commission

    @api.depends('sale_id.amount_total', 'commission')
    def _compute_amount(self):
        for rec in self:
            rec.amount = rec.sale_id.amount_total * (rec.commission / 100)
