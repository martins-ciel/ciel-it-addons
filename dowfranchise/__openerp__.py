# -*- coding: utf-8 -*-
{
    'name': "Ciel IT - Dow Franchise",
    'summary': "Controle dos formulários de franchise",
    'description': "Controle dos formulários de franchise",
    'author': "Rafael Petrella",
    'website': "http://ciel-it.com",
    'category': 'Uncategorized',
    'version': '8.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [
        'security/dowfranchise_security.xml',
        'security/ir.model.access.csv',
        'views/dowfranchise.xml',
    ],

    'installable' : True,
    'application' : True,
}
