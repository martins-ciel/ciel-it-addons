# -*- encoding: utf-8 -*-
##############################################################################
#
#    Samples module for Odoo Qweb Report
#    Copyright (C) 2016- XUBI.ME (http://www.xubi.me)
#    @author binhnguyenxuan (https://www.linkedin.com/in/binh-nguyen-xuan-46556279)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Ciel IT Qweb Report',
    'summary': 'Report module for Odoo',
    'version': '8.0.1.0.0',
    'category': 'Report',
    'description': """
Report module for Odoo

==================================================

Functionality:
--------------
    * Report module for Odoo Qweb Report

Copyright, Authors and Licence:
-------------------------------
    * Author:
        * Rafael Petrella
    * Licence: AGPL-3 (http://www.gnu.org/licenses/);""",
    'author': "Rafael Petrella",
    'website': 'http://ciel-it.com',
    'license': 'AGPL-3',
    'depends': [
        'sale',
    ],
    'data': [
        'report/sale_order_report_without_prices.xml',
       'report/sale_order_report_with_prices.xml',
    ],
    'qweb': [
    ],
    'installable': True,
}
