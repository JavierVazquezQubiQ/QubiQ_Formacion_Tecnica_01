# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import api, fields, models, _


class SaleCommission(models.Model):
    _name = 'sale.commission'
    _description = _('Sale Commission')

    name = fields.Many2one(
        string=_('Commercial'),
        comodel_name="res.partner",
        domain="[('is_commercial', '=', True)]"
    )
    commission = fields.Float(
        string=_('% Commission')
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
