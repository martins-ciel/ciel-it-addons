# -*- coding: utf-8 -*-
{
    'name': "Ciel IT - Dow Freight",
    'summary': "Calculo para Distribuição de Transportadoras",
    'description': "Sistema para distribuição de entregas entre as transportadoras cadastradas",
    'author': "Rafael Petrella",
    'website': "http://ciel-it.com",
    'category': 'Uncategorized',
    'version': '8.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [
        'security/dowfreight_security.xml',
        'security/ir.model.access.csv',
        'views/dowfreight.xml',
    ],

    'installable' : True,
    'application' : True,
}
