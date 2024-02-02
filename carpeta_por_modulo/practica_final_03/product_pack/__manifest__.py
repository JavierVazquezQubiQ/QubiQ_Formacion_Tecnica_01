# Copyright 2024 Javier Vázquez <javier.vazquez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

{
    "name": "Product Packs",
    "summary": "Product Packs",
    "version": "16.0.1.0.0",
    "category": "Product",
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
        'views/sale_order.xml',
        'reports/report_product_template.xml',
        'reports/reports.xml',
    ],
    "images": ['static/description/icon.png'],
    'web_icon': ['static/description/icon.png'],
}
