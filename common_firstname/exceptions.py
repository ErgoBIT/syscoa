# -*- encoding: utf-8 -*-
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

from openerp import _, exceptions


class EmptyNamesError(exceptions.ValidationError):
    def __init__(self, record, objname, value=_("No name is set.")):
        self.record = record
        self._value = value
        self.name = _("Error(s) with " + objname + " %d's name.") % record.id 
        self.args = (self.name, value)
