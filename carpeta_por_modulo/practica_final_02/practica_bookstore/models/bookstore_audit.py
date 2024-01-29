# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api


class BookstoreAudit(models.Model):
    _name = "bookstore.audit"
    _description = 'Bookstore audit'

    action_type = fields.Selection([
        ('create', 'Creation'),
        ('write', 'Modification'),
        ('unlink', 'Deletion')],
        readonly=True
    )

    date_time = fields.Datetime()
    user_id = fields.Many2one('res.users')
    book_id = fields.Many2one('bookstore')
    book_name = fields.Char()
