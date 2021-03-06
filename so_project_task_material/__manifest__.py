# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################


{
    'name': 'SO Project Task Material',
    'author': 'Aardug',
    'website': 'http://www.aardug.nl',
    'category': 'Project',
    'summary': '',
    'version': '13.0.1.0',
    'description': """
        This module aims to syncronise sale order task material with project task material.
        BOM product also can add on sale order and update qty on consumed material and order picking
        """,
    'depends': ['sale_timesheet', 'purchase','mrp'],
    'data': [
        'security/ir.model.access.csv',
        'data/task_custom_header.xml',
        'report/task_report.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
        'views/task_view.xml',
    ],
    'installable': True,
}
