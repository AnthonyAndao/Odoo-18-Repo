# -*- coding: utf-8 -*-
{
    'name': "Hotel Management System",
    'summary': "Hotel Management System",
    'description': "Hotel Guest Registration and Billing System",
    'author': "Warlter Andao",
    'website': "github.com/WarlterAndao",


    'category': 'Uncategorized',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mainmenu.xml',
        'views/charges.xml',
        'views/roomtypes.xml',
        'views/rooms.xml',
        'views/guests.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}