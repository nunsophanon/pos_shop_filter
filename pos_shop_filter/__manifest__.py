# -*- coding: utf-8 -*-
{
    'name': "POS Shop filter",
    'version': '1.0',
    'category': 'Sale/Point of Sale',
    'summary': """
        Generate Sale Price for products
        """,
    'license': 'OPL-1',
    'images': [
        'static/description/main_screenshot.png',
    ],
    'description': """
        This module is allow admin to assign Point of Sale to each employee or owner
    """,

    'author': "ERP CAMBODIA, Nun Sophanon",
    'website': "http://www.erpcambodia.biz",
    'maintainer': 'ERP CAMBODIA',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],
    'support': 'erpcambo@gmail.com',
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'qweb': [
    ],
    'installable': True,
}
