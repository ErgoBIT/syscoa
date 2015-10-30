# -*- coding: utf-8 -*-
##############################################################################
#
#    SYSCOA Company
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
from openerp import models, fields, api, _
import time
from openerp.tools.translate import _



class account_fiscalyear(models.Model):
    _inherit = 'account.fiscalyear'
    
    boolean = fields.Boolean(string='Boolean')
    
    @api.model
    def create(self, vals):
        res = super(account_fiscalyear,self).create(vals)
        obj = self.browse(res.id)
        obj.boolean = True
        line_note = {}
        line_front = {}
        dir_vals =[]
        sh_vals = []
        con_vals = []
        fact_finance_note_obj = self.env['fact.finance.note']
        frontpage_obj = self.env['frontpage']
        fiscalyear_id = self.env['account.fiscalyear'].find()
        note_search_rec = fact_finance_note_obj.search([('fiscalyear_id','=', fiscalyear_id)])
        frontpage_rec = frontpage_obj.search([('fiscalyear','=', fiscalyear_id)])
        for record in note_search_rec:
            line_note = {
                        'fiscalyear_id': res.id,
                        'company_id': record.company_id.id or '',
                        'note_text': '',
                        'account': record.account.id or '',
                        'root_account': record.root_account.id or '',
                        'note_id': record.note_id or ''
                    }
            note_copy_id = fact_finance_note_obj.create(line_note)
        for rec in frontpage_rec:
            for dir_rec in rec.dir_hr_emp_ids:
                dir_vals.append((0,0,{
                       'firstname': dir_rec.firstname or '',
                       'lastname': dir_rec.lastname or '', 
                       'job_id': dir_rec.job_id.id or ''
                       }))
            for sh_rec in rec.shareholders_ids:
                sh_vals.append((0,0,{
                           'firstname': sh_rec.firstname or '',
                           'name': sh_rec.name or '',
                           'stakeholder_country_id': sh_rec.stakeholder_country_id.id or '',
                           'stakeholder_capital_amount': sh_rec.stakeholder_capital_amount or 0.0,
                           'stakeholder_capital_percentage': sh_rec.stakeholder_capital_percentage or 0.0
                           }))
            for con_rec in rec.con_hr_emp_ids:
                con_vals.append((0,0,{
                       'firstname': con_rec.firstname or '',
                       'lastname': con_rec.lastname or '', 
                       'job_id': con_rec.job_id.id or ''
                       }))
            line_front = {
                    'fiscalyear': res.id,
                    'actual_closing_date' : rec.actual_closing_date or False,
                    'perc_production_capa_used' : rec.perc_production_capa_used or 0.0,
                    'contact_person' : rec.contact_person.id or '',
                    'professional_person' : rec.professional_person.id or '',
                    'public_accountant_1' : rec.public_accountant_1.id or '',
                    'public_accountant_2' : rec.public_accountant_2.id or '',
                    'certified' : rec.certified or '',
                    'approved' : rec.approved or '',
                    'signee' : rec.signee.id or '',
                    'signing_date' : rec.signing_date or False,
                    'legal_form' : rec.legal_form or '',
                    'fiscal_regime' : rec.fiscal_regime or '',
                    'head_office_country' : rec.head_office_country or '',
                    'branches_in_country' : rec.branches_in_country or 0,
                    'branches_out_country' : rec.branches_out_country or 0,
                    'executives' : rec.executives.id or '',
                    'administratives' : rec.administratives.id or '',
                    'dir_hr_emp_ids': dir_vals,
                    'shareholders_ids': sh_vals,
                    'con_hr_emp_ids': con_vals
                                    }
            frontpage_id = frontpage_obj.create(line_front)
        return res
    
    
    
    
    