# -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt. Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Product Manufacturing MRP Dashboard",
    'version': '3.1.2',
    'category': 'Manufacturing/Manufacturing',
    'license': 'Other proprietary',
    'price': 9.0,
    'currency': 'EUR',
    'summary':  """Product Manufacturing Dashboard in Odoo.""",
    'description': """
Product Manufacturing Dashboard
Product dashboard
Product view
Product Manufacturing board
Product Manufacturing view
Product kanban
    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/img.png'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/product_manufacturing_dashboard/907',#'https://youtu.be/8p98JPOHjAo',
    'depends': [
        'mrp',
    ],

    'data': [
        'views/product_mo_dashboard_view.xml',
    ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
