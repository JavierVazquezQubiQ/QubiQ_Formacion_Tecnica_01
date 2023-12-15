# Copyright 2023 - Javier Vázquez Flores

from odoo import fields, models, api


class BookstoreAudit(models.Model):
    _name = "bookstore.audit"
    _description = 'Bookstore audit'

    action_type = fields.Selection([
        ('create', 'Creation'),
        ('write', 'Modification'),
        ('unlink', 'Deletion')],
        string='Action Type',
        readonly=True
    )

    date_time = fields.Datetime(string='Date and time')
    user_id = fields.Many2one('res.users', string='User')
    book_id = fields.Many2one('bookstore', string='Book_id')
    book_name = fields.Char(string='Book Name')
