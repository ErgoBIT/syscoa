# -*- coding: utf-8 -*-
###########################################################################
#
#    Common Firstname for partner and employee
#
#    Copyright (C) 2014-TODAY ErgoBIT Consulting SARL (<http://www.ergobit.org>).
#    All Rights Reserved.
#    contact: info@ergobit.org
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
    'name': 'First name and last name',
    'summary': "Split first name and last name for non company partners and employees",
    'version': '1.0',
    'author': "ErgoBIT Consulting",
    'maintainer': 'ErgoBIT',
    'category': 'Extra Tools',
    'website': 'http://www.ergobit.org',
    'depends': ['base', 'hr'], 
    'data': [
        'views/res_partner.xml',
        'views/res_user.xml',
        'views/hr_employee.xml',
        'data/res_partner.yml',
#        'data/hr_employee.yml',
    ],
    'demo': [],
    'test': [],
    'auto_install': False,
    'installable': True,
    'images': []
}
