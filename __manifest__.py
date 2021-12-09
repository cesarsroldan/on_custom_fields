# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyrig# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'custom fields and mods',
    'version': '0.1',
    'category': 'sale',
    # 'sequence': 15,
    'summary': 'custom fields and mods',
    'description': """
        Custom fields and little modifications for Vivanti 
    """,
    'author': 'Xetechs, S.A.',
    'website': 'https://www.xetechs.com',
    'depends': ['base_setup', 'sale', 'purchase'],
    'data': [
        'views/views.xml',
        'views/purchase_country_view.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
