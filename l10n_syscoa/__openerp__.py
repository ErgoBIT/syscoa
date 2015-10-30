# -*- coding: utf-8 -*-
##############################################################################
#
#    SYSCOA Accounting Chart
#    Copyright (C) 2014-TODAY ERGOBIT Consulting SARL (<http://www.ergobit.org>).
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
    'name' : 'SYSCOA - Accounting',
    'version' : '1.1',
    'author' : 'ERGOBIT Consulting',
    'category' : 'Localization/Account Charts',
    'description': """
SYSCOA accounting chart as per 2014.
====================================  
This accounting chart is valid from 2014 on in all UEMOA countries according to the agreement of CCOA (Conseil Comptable Ouest Africain), a commission of the SYSCOA. 

The countries members of the SYSCOA are the following:
    - Benin, Burkina Faso, Ivory Coast, Guinea Bissau, Mali, Niger, Senegal, Togo.
    

We've also implemented an other localization module which can generate the whole set of legal reports:
    - balance sheet report
    - profit and lost report
    - cashflow report
    - Notes/Comments
    - and all others...
    
Please contact us if you need any help: consulting@ergobit.org
    """,
    
    'website': 'http://www.ergobit.org',
    'depends' : ['account', 'base_vat'],
    'demo' : [],
    'data' : [
        'data/account_types.xml',
        'data/account_chart.xml',
        'data/account_tax_code.xml',
        'data/account_tax.xml',
        'wizard/l10n_syscoa_wizard.xml',
        
        'data/res.country.group.csv',
        ],
    'auto_install': False,
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
