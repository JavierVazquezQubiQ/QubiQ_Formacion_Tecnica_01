# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models, _


class BookstoreAudit(models.Model):
    _name = "bookstore.audit"
    _description = _('Bookstore audit')

    action_type = fields.Selection(
        selection=[
            ('create', _('Creation')),
            ('write', _('Modification')),
            ('unlink', _('Deletion'))
        ],
        readonly=True
    )

    date_time = fields.Datetime()
    user_id = fields.Many2one('res.users')
    book_id = fields.Many2one('bookstore')
    book_name = fields.Char()
