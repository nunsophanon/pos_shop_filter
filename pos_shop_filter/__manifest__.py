# -*- coding: utf-8 -*-
{
    'name': "POS Shop filter",
    'version': '1.0',
    'category': 'Sale/Point of Sale',
    'summary': """
        Generate Sale Price for products
        """,

    'description': """
        This module is allow user to genrate Sale Price for their products
    """,

    'author': "ERP Cambodia Co,.LTD",
    'website': "http://www.erpcambodia.biz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'qweb': [
    ],
    'installable': True,
}
