# -*- coding: utf-8 -*-
{
    'name': "Ciel IT - Machine Application",
    'summary': "Carga Máquina",
    'description': "Carga Máquina",
    'author': "Rafael Petrella",
    'website': "http://ciel-it.com",
    'category': 'Uncategorized',
    'version': '8.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [
        'security/machineapp_security.xml',
        'security/ir.model.access.csv',
        'views/machineapp.xml',
    ],

    'installable' : True,
    'application' : True,
}
