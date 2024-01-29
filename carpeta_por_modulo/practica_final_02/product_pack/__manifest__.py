# Copyright 2023 - Javier Vázquez Flores

{
    "name": "Practica Final 02 - Product Packs",
    "summary": "Product Packs",
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
        'views/product_template.xml',
        'views/product_pack_line.xml',
        'reports/report_product_template.xml',
        'reports/reports.xml',
    ],
    "images": ['static/description/icon.png'],
    'web_icon': ['static/description/icon.png'],
}
