# -*- coding: utf-8 -*-
############################################################################
#
#    Company Information according to SYSCOA regulation for West Africa
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
    'name' : 'SYSCOA Company',
    'category' : 'Company',
    'description' : """This module provide the information about Company,
    Company Activities and Company Branches (according to SYSCOA regulation)""",
    'version' : '1.10',
    'author' : 'ErgoBIT Consulting',
    'website': 'http://www.ergobit.org',
    'depends' : ['base', 'sale', 'account', 'common_firstname'],
    'data' : [
        'fact_frontpage_view.xml',
    ],
    'installable' : True,
    'auto_install' : False,
    'application' : True
}