# -*- coding: utf-8 -*-
{
    'name': "Minesweeper",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "E Lebedev",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/minesweaper_players_view.xml',
        'views/minesweaper_games_view.xml',
        'views/minesweaper_fields_view.xml',
        'views/minesweaper_awards_view.xml',


        'views/minesweeper_menus_view.xml',

        'security/ir.model.access.csv',
        'data/minesweeper.fields.csv',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',


    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
