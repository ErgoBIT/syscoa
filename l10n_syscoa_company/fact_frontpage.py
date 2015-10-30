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

class res_company(models.Model):
    _inherit = 'res.company'
    _rec_name = 'company_acronym'
   
    company_acronym = fields.Char('Company Acronym')
    code_importer = fields.Char('Code Importer')
    code_activity_principal = fields.Char('Code Activity Principal')
    name_activity_pincipal = fields.Char('Name Activity Pincipal')
    office = fields.Char('Office', size=5, default='0')
    social_registry_id = fields.Char('Social Registry')
    fiscal_id = fields.Char('Fiscal')
    first_fiscalyear_in_country = fields.Char('First Fiscalyear In Country',size=4)
    controlled_by = fields.Selection([('A','public'),('B','prive national'),('C','prive etranger')],'Controlled By')
    branches = fields.One2many('company.branche','company_id','Branches')
    company_activities = fields.One2many('company.activity','company_id','Company Activities')


class res_partner(models.Model):
    _inherit = 'res.partner'
    
    @api.multi
    def set_name(self, firstname, lastname):
#b        res = {}
#b        if firstname or lastname:
#b            if not lastname:
#b                lastname = " "
#b                full_name = str(firstname)+ " " + str(lastname)
#                res.update({'name':full_name})
#            if firstname and lastname:
#                full_name = str(firstname)+ " " + str(lastname)
#                res.update({'name':full_name})
#        else:
#            res.update({'name':" "})
#b        return {"value":res}
        pass
 
    
#b    name = fields.Char('Name', required=True, select=True, default=" ")
#b    first_name = fields.Char("First Name")
#b    last_name = fields.Char("Last Name")
    stakeholder = fields.Boolean("Stakeholder")
    stakeholder_country_id = fields.Many2one('res.country','Stakeholder Country')
    stakeholder_capital_amount = fields.Float("Stakeholder Capital Amount")
    stakeholder_capital_percentage = fields.Float("Stakeholder Capital Percentage")
#b    firstname = fields.Char("First Name")
#b    lastname = fields.Char("Last Name")
        
        
class company_branche(models.Model):
    _name="company.branche"
    
    @api.model
    def get_company(self):
        company_id = self.env['res.users'].browse(self._context['uid']).company_id.id
        return company_id
    
    company_id = fields.Many2one('res.company','Company', default=get_company)
    name = fields.Char('Name')
    country_id = fields.Many2one('res.country','Country')
    capital_amount = fields.Float('Capital Amount')
    capital_percentage = fields.Float("Capital Percentage")
    
    
class company_activity(models.Model):
    _name = "company.activity"
    
    @api.model
    def get_company(self):
        company_id = self.env['res.users'].browse(self._context['uid']).company_id.id
        return company_id
    
    company_id = fields.Many2one('res.company','Company', default=get_company)
    name = fields.Char('Name')
    code = fields.Char('Code', size=7)
    turnover_addedvalue = fields.Float('Turnover')
    percentage = fields.Float('Percentage')
    
    
class frontpage(models.Model):
    _name = "frontpage"
    
    @api.model
    def get_company(self):
        company_id = self.env['res.users'].browse(self._context['uid']).company_id.id
        return company_id
    
    @api.model
    def get_fiscalyear(self):
        fiscalyear_id = self.env['account.fiscalyear'].find()
        return fiscalyear_id
    
    @api.multi
    def _check_company_fiscalyear(self):
        search_id = [rec.id for rec in self.search([])]
        search_id.remove(self.ids[0])
        for rec in self.browse(self.ids):
            for line in self.browse(search_id):
                if rec.company_id.id == line.company_id.id and rec.fiscalyear.id == line.fiscalyear.id:
                    return False
        return True
    
    company_id = fields.Many2one('res.company','Company', default=get_company)
    fiscalyear = fields.Many2one('account.fiscalyear','Fiscalyear' , default=get_fiscalyear)
    actual_closing_date = fields.Date('Actual Closing Date')
    perc_production_capa_used = fields.Float('Perc Production Capa Used')
    contact_person = fields.Many2one('hr.employee','Contact Person')
    professional_person = fields.Many2one('hr.employee','Professional Person')
    public_accountant_1 = fields.Many2one('res.partner','Public Accountant 1')
    public_accountant_2 = fields.Many2one('res.partner', 'Public Accountant 2')
    certified = fields.Selection([('A','NOn assujetti'),('B','Non (refus)'),('C','Oui avecreserv'),('D', 'Ouisans reserves')],'Certified')
    approved = fields.Selection([('A','Non assujetti'), ('B','Non'), ('C','Oui')],'Approved')
    signee = fields.Many2one('hr.employee','Signee')
    signing_date = fields.Date('Signing Date')
    legal_form = fields.Char('Legal Form')
    fiscal_regime = fields.Char('Fiscal Regime')
    head_office_country = fields.Char('Head Office Country')
    branches_in_country = fields.Integer('Branches In Country')
    branches_out_country = fields.Integer('Branches Out Country')
    executives = fields.Many2one('hr.employee','Executives')
    administratives = fields.Many2one('hr.employee','Administratives')
    shareholders_ids = fields.Many2many('res.partner', 'frontpage_parent_rel', 'frontpage_id', 'patner_id', 'Parent')
    con_hr_emp_ids = fields.Many2many('hr.employee', 'con_hr_employee_rel','frontpage_id', 'employee_id', 'Employee')
    dir_hr_emp_ids = fields.Many2many('hr.employee', 'dir_hr_employee_rel','frontpage_id', 'employee_id', 'Employee')
    
    _constraints = [(_check_company_fiscalyear,_('Vous avez pour ce tableau un autre rapport en cours dans cet exercice fisal. Veuillez continuer avec celui ci.'),['company_id'])]


class hr_employee(models.Model):
    _inherit = 'hr.employee'
    
#B    firstname = fields.Char('Name')
#B    lastname = fields.Char('Lastname')
    
#B    @api.model
#B    def create(self, values):
#        # Create same Employee automatically when create new user.
#        if values.get('firstname') and values.get('lastname'):
#            name = values.get('firstname') + ' ' + values.get('lastname')
#            values.update({'name' : name})
#            return super(hr_employee, self).create(values)
    
#    _sql_constraints = [("company_must_unique","unique(company_id)","Company Must be Unique")]


class res_user_name(models.Model):
    _inherit = 'res.users'
    
#b    name = fields.Char('Name', required=True, select=True, default=" ")
#b    firstname = fields.Char('Firstname')
#b    lastname = fields.Char('Lastname')
    
    @api.multi
    def user_full_name(self, firstname, lastname):
#b        res = {}
#        if firstname or lastname:
#            full_name = str(firstname) + " " + str(lastname)
#            res.update({'name':full_name})
#        else:
#            res.update({'name':" "})
#b        return {'value':res}
        pass
    
#B    @api.model
#B    def create(self, values):
#        # Create same Employee automatically when create new user.
#        if values.get('firstname') and values.get('lastname'):
#            name = values.get('firstname') + ' ' + values.get('lastname')
#            values.update({'name' : name})
#            print "sbssackcawsc", values
#            self.env['hr.employee'].create(values)
#            return super(res_user_name, self).create(values)
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
    