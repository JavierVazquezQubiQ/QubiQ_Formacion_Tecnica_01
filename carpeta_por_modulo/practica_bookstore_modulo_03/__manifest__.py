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
    "depends": ['base'],
    "data": ['security/ir.model.access.csv',
             'views/bookstore.xml',
             'views/res_partner.xml',
             ],
}