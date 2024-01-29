# Copyright 2023 - Javier Vázquez Flores

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    component_line_ids = fields.One2many(
        comodel_name='product.pack.line',
        inverse_name='pack_id',
        string='Pack Components Lines'
    )
    is_pack = fields.Boolean(
        string='Is Pack'
    )
    price_pack_method = fields.Selection(
        string='Cost Calculation',
        selection=[
            ('normal_price', 'Normal Price'),
            ('component_total', 'Sum Components'),
            ],
        default="normal_price"
    )
    components_price = fields.Float(
        compute="_compute_price_pack",
        store=True,
        readonly=False,
    )

    @api.depends('price_pack_method', 'component_line_ids')
    def _compute_price_pack(self):
        for rec in self:
            if rec.price_pack_method == 'component_total':
                rec.components_price = self.list_price
                for line in rec.component_line_ids:
                    rec.components_price += line.quantity * line.price
            else:
                rec.components_price = rec.list_price or 0
