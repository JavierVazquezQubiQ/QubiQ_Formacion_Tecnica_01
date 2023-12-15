# Copyright 2023 - Javier Vázquez Flores

{
    "name": "Bookstore",
    "summary": "Register books to have a bookstore in Odoo",
    "version": "16.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['base', 'product', 'sale'],
    "data": ['security/ir.model.access.csv',
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
