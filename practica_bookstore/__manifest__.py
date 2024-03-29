# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

{
    "name": "Bookstore",
    "summary": "Register books to have a bookstore in Odoo",
    "version": "16.0.1.0.0",
    "category": "Product",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['base', 'product', 'sale'],
    "data": ['security/security.xml',
             'security/ir.model.access.csv',
             'reports/layout.xml',
             'reports/report_bookstore.xml',
             'reports/report_sale.xml',
             'reports/reports.xml',
             'views/bookstore_audit.xml',
             'views/bookstore_genre.xml',
             'views/bookstore_packs.xml',
             'views/bookstore.xml',
             'views/menu.xml',
             'views/res_partner.xml',
             ],
    "images": ['static/description/icon.png'],
    'web_icon': ['static/description/icon.png'],
}
