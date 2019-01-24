# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_physician(models.Model):
    _name="medical.physician"
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner','Medico',required=True)
    institution_partner_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string='Institucion')
#   speciality_id = fields.Many2one('medical.speciality','Especialidad',required=False)
    code = fields.Char('MAT. PROFESIONAL')
    code_esp = fields.Char('REG. ESPECIALIDAD')
    code_colmed = fields.Char('REG. COLMED SCZ')
    nom_especialidad = fields.Char('NOMBRE DE ESPECIALIDAD')
    info = fields.Text('Informacion Extra')
