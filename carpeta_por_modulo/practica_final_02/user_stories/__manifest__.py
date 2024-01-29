# Copyright 2023 - Javier Vázquez Flores

{
    "name": "User Stories",
    "summary": "Register user stories in Odoo",
    "version": "16.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'base',
        'product',
        'sale',
        'contacts',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'reports/report_sale.xml',
    ],
    "images": ['static/description/icon.png'],
    'web_icon': ['static/description/icon.png'],
}
