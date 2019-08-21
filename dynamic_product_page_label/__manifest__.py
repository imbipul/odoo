# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': "Dynamic Product Page Label",
    'version': '1.1',
    'category': 'Product',
    'description': """Dynamic Product Page Label.""",
    'summary': 'Create custom page label template by frontend and print dynamic product page label report.',
    'author': 'Acespritech Solutions Pvt.Ltd',
    'website': 'http://www.acespritech.com',
    "depends": ['sale_management', 'base', 'purchase', 'stock', 'account'],
    'price': 149, 
    'currency': 'EUR',
    "data": [
        'views/wizard_product_page_report_view.xml',
        'page_reports.xml',
        'security/ir.model.access.csv',
        'views/dynamic_prod_page_rpt.xml',
        'data/design_data.xml'
    ],
    'images': ['static/description/main_screenshot.png'],
    "installable": True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
