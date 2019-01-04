# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class res_partner(models.Model):
    _inherit = 'res.partner'

    relationship = fields.Char(string='Relacion')
    relative_partner_id = fields.Many2one('res.partner',string="Id_relativo")
    is_patient = fields.Boolean(string='Paciente')
    is_person = fields.Boolean(string="Persona")
    is_doctor = fields.Boolean(string="Doctor")
    is_insurance_company = fields.Boolean(string='Compañoia aseguradora')
    is_pharmacy = fields.Boolean(string="Farmacia")
    patient_insurance_ids = fields.One2many('medical.insurance','patient_id')
#     domiciliary_id = fields.Many2one('medical.domiciliary.unit')
    is_institution = fields.Boolean('Institucion')
    company_insurance_ids = fields.One2many('medical.insurance','insurance_compnay_id','Seguro')
    reference = fields.Char('Numero ID')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: