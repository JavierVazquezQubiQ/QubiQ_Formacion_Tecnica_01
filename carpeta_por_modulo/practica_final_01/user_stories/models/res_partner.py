# Copyright 2023 - Javier Vázquez Flores

from odoo import api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_commercial = fields.Boolean(
        string='Commercial'
    )
    commercial_code = fields.Char(
        copy=False
    )
    commission = fields.Float(
        string='% Commission'
    )

    _sql_constraints = [
        ('commercial_code_uniq', 'unique (commercial_code)',
         'The commercial code must be unique!')
    ]

    def unlink(self):
        # Mapped itera sobre un recordset para agrupar un campo en una lista
        if any(self.mapped('commercial_code')):
            raise UserError("You can not delete a contact with"
                            " a Commercial Code")
        # Es lo mismo que hacer
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
