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
        string=_('Action Type'),
        readonly=True
    )

    date_time = fields.Datetime(
        string=_('Date Time')
    )
    user_id = fields.Many2one(
        'res.users',
        string=_('User ID')
    )
    book_id = fields.Many2one(
        'bookstore',
        string=_('Book ID')
    )
    book_name = fields.Char(
        string=_('Book Name')
    )
