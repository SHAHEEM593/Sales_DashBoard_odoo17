# -*- coding: utf-8 -*-
{
    'name': "Sales DashBoard",
    'version': '17.0.1.0.0',
    'depends': ['sale_management'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Sales DashBoard
    """,
    'summary': 'Sales DashBoard',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/sale_order_view_menu_data.xml',
        'views/sale_order_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'sales_dashboard/static/src/js/client_action_views.js',
            'sales_dashboard/static/src/xml/advanced_dashboard.xml',
            'sales_dashboard/static/src/css/style.css',
        ],
    },

    'application': True,
    'installable': True,


}
