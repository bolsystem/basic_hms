# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_insurance(models.Model):
    _name = 'medical.insurance'
    _rec_name = 'insurance_compnay_id'

    number = fields.Char('Numero')
    medical_insurance_partner_id = fields.Many2one('res.partner','Propietario',required=True)
    patient_id = fields.Many2one('res.partner', 'Pertenece a')
    type =  fields.Selection([('state','Estado'),('private','Privado'),('labour_union','Sindicato Laboral / Sindical')],'Tipo de seguro')
    member_since= fields.Date('Miembro desde')
    insurance_compnay_id = fields.Many2one('res.partner',domain=[('is_insurance_company','=',True)],string='Compañia aseguradora')
    category = fields.Char('Categoria')
    notes= fields.Text('Info extra')
    member_exp = fields.Date('Fecha de expiracion')
    medical_insurance_plan_id = fields.Many2one('medical.insurance.plan','Plan')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
