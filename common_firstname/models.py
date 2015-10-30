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

import logging
from openerp import api, fields, models
from . import exceptions


_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    """Adds last name and first name; name becomes a stored function field."""
    _inherit = 'res.partner'

    firstname = fields.Char("First name")
    lastname = fields.Char("Last name")
    name = fields.Char(
        compute="_compute_name",
        inverse="_inverse_name_after_cleaning_whitespace",
        required=False,
        store=True)


    @api.one
    @api.depends("firstname", "lastname")
    def _compute_name(self):
        """Write the 'name' field according to splitted data."""
        if self.lastname:
            self.lastname = self.lastname.upper()
        if self.firstname:
            self.firstname = self.firstname.title()
        self.name = u" ".join((p for p in (self.firstname,
                                           self.lastname) if p))

    @api.one
    def _inverse_name_after_cleaning_whitespace(self):
        """Clean whitespace in :attr:`~.name` and split it.

        Removes leading, trailing and duplicated whitespace.

        The splitting logic is stored separately in :meth:`~._inverse_name`, so
        submodules can extend that method and get whitespace cleaning for free.
        """
        # Remove unneeded whitespace
        clean = u" ".join(self.name.split(None)) if self.name else self.name

        # Clean name avoiding infinite recursion
        if self.name != clean:
            self.name = clean

        # Save name in the real fields
        else:
            self._inverse_name()


    @api.one
    def _inverse_name(self):
        """Try to revert the effect of :meth:`._compute_name`.

        - If the partner is a company, save it in the lastname.
        - Otherwise, make a guess.

        This method can be easily overriden by other submodules.

        When this method is called, :attr:`~.name` already has unified and
        trimmed whitespace.
        """
        # Company name goes to the lastname
        if self.is_company or self.name is False:
            parts = [self.name, False]
        # Guess name splitting
        else:
            if not self.firstname:
                parts = self.name.split(" ")
                if len(parts) > 1:     
                    self.lastname = parts.pop()            
                    self.firstname = u" ".join(fn for fn in parts)
            if self.lastname:
                self.lastname = self.lastname.upper()
            if self.firstname:
                self.firstname = self.firstname.title()


    @api.one
    @api.constrains("firstname", "lastname")
    def _check_name(self):
        """Ensure at least one name is set."""
        if not (self.firstname or self.lastname):
            raise exceptions.EmptyNamesError(self, objname="partners")

    @api.one
    @api.onchange("name")
    def _onchange_name(self):
        """Ensure :attr:`~.name` is inverted in the UI."""
        self._inverse_name_after_cleaning_whitespace()

    @api.model
    def _install_partner_firstname(self):
        """Save names correctly in the database.

        Before installing the module, field ``name`` contains all full names.
        When installing it, this method parses those names and saves them
        correctly into the database. This can be called later too if needed.
        """
        # Find records with empty firstname and lastname
        records = self.search([("firstname", "=", False),
                               ("lastname", "=", False)])

        # Force calculations there
        records._inverse_name()
        _logger.info("%d partners updated installing module.", len(records)) 



#class HrEmployee(models.Model):
#    """Adds last name and first name; name becomes a stored function field."""
#    _inherit = 'hr.employee'

class Resource(models.Model):
    """Adds last name and first name; name becomes a stored function field."""
    _inherit = 'resource.resource'

    firstname = fields.Char("First name")
    lastname = fields.Char("Last name")
    name = fields.Char(
        compute="_compute_name",
        inverse="_inverse_name_after_cleaning_whitespace",
        required=False,
        store=True)

    @api.one
    @api.depends("firstname", "lastname")
    def _compute_name(self):
        """Write the 'name' field according to splitted data."""
        if self.lastname:
            self.lastname = self.lastname.upper()
        if self.firstname:
            self.firstname = self.firstname.title()
        self.name = u" ".join((p for p in (self.firstname,
                                           self.lastname) if p))

    @api.one
    def _inverse_name_after_cleaning_whitespace(self):
        """Clean whitespace in :attr:`~.name` and split it.

        Removes leading, trailing and duplicated whitespace.

        The splitting logic is stored separately in :meth:`~._inverse_name`, so
        submodules can extend that method and get whitespace cleaning for free.
        """
        # Remove unneeded whitespace
        clean = u" ".join(self.name.split(None)) if self.name else self.name

        # Clean name avoiding infinite recursion
        if self.name != clean:
            self.name = clean

        # Save name in the real fields
        else:
            self._inverse_name()


    @api.one
    def _inverse_name(self):
        """Try to revert the effect of :meth:`._compute_name`.

        - If the partner is a company, save it in the lastname.
        - Otherwise, make a guess.

        This method can be easily overriden by other submodules.

        When this method is called, :attr:`~.name` already has unified and
        trimmed whitespace.
        """
#        if not self.firstname:
#        parts = self.name.split(" ") 
#        if len(parts) > 1:     
#            self.lastname = parts.pop()  
#            self.firstname = u" ".join(fn for fn in parts) 
#        if self.lastname:
#            self.lastname = self.lastname.upper()
#        if self.firstname:
#            self.firstname = self.firstname.title()

        # Company name goes to the lastname
        if self.resource_type == 'material' or self.name is False:
            parts = [self.name, False]
        # Guess name splitting
        else:
            if not self.firstname:
                parts = self.name.split(" ")
                if len(parts) > 1:     
                    self.lastname = parts.pop()            
                    self.firstname = u" ".join(fn for fn in parts)
            if self.lastname:
                self.lastname = self.lastname.upper()
            if self.firstname:
                self.firstname = self.firstname.title()


    @api.one
    @api.constrains("firstname", "lastname")
    def _check_name(self):
        """Ensure at least one name is set."""
        if not (self.firstname or self.lastname):
            raise exceptions.EmptyNamesError(self, objname="employees")
            pass

    @api.one
    @api.onchange("name")
    def _onchange_name(self):
        """Ensure :attr:`~.name` is inverted in the UI."""
        self._inverse_name_after_cleaning_whitespace()  

    @api.model
    def _install_employee_firstname(self):
        """Save names correctly in the database.

        Before installing the module, field ``name`` contains all full names.
        When installing it, this method parses those names and saves them
        correctly into the database. This can be called later too if needed.
        """
        # Find records with empty firstname and lastname
        records = self.search([("firstname", "=", False),
                               ("lastname", "=", False)])

        # Force calculations there
        records._inverse_name()
        _logger.info("%d partners updated installing module.", len(records))


