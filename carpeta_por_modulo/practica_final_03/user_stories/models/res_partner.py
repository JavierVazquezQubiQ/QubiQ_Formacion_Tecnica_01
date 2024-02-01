# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_commercial = fields.Boolean()
    commercial_code = fields.Char(
        copy=False
    )
    commission = fields.Float(
        string=_('% Commission')
    )

    _sql_constraints = [
        ('commercial_code_uniq', 'unique (commercial_code)',
         _('The commercial code must be unique!'))
    ]

    def unlink(self):
        # Mapped iterates over a recordset to group a field into a list.
        if any(self.mapped('commercial_code')):
            raise UserError(_(
                "You can not delete a contact with a Commercial Code"
            ))
        # It is the same as doing
        # for rec in self:
        #     if rec.commercial_code:
        #         raise
        res = super().unlink()
        return res

    @api.onchange('is_commercial')
    @api.constrains('is_commercial')
    def _check_sales_person(self):
        for record in self:
            if record.is_commercial:
                record.commission = 10.00
            else:
                record.commission = 0.0
