# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    component_line_ids = fields.One2many(
        comodel_name='product.pack.line',
        inverse_name='pack_id',
        string=_('Pack Components Lines')
    )
    is_pack = fields.Boolean()
    price_pack_method = fields.Selection(
        string=_('Cost Calculation'),
        selection=[
            ('normal_price', _('Normal Price')),
            ('component_total', _('Sum Components')),
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
