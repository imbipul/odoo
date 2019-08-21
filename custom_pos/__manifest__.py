# -*- coding: utf-8 -*-
{
    'name': "Custom POS",
    'summary': """
        Customized Point of Sale
    """,
    'description': """
        Customized Point of Sale
    """,
    'author': "Abdullah Al Arafat Bipul",
    'website': "http://www.scorpion9.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}