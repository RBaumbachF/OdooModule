# -*- coding: utf-8 -*-
{
    'name': "Casa de la Cultura",

    'summary': """
        Gestiona las actividades de una Casa de la Cultura""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ruth Baumbach",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_usuarios.xml',
        'reports/report_actividades.xml',
        'reports/report_reservas.xml',
        'reports/report_pagos.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}
