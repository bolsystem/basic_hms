# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_diseases(models.Model):
    _name = 'medical.patient.diseases'
    
#     new_born_id = fields.Many2one('medical.newborn')
    pathelogh_id = fields.Many2one('medical.pathology', 'Enfermedad')
    status_of_the_disease = fields.Selection([('chronic','Cronica'),('status quo','Estatus quo'),('healed','Curado'), ('improving','Mejorando'), ('worsening', 'Empeorando') ], 'Estado de la Enfermedad')
    is_active = fields.Boolean('Enfermedad activa')
    diagnosed_date = fields.Date('Fecha de diagnostico')
    age = fields.Date('Edad cuando se diagnostico')
    disease_severity = fields.Selection([('mild','Media'), ('moderate','Moderada'), ('severe','Severa')], 'Severidad')
    is_infectious = fields.Boolean('Enfermedad infecciosa', help = 'Revis si el paciente tiene una Enfermedad infecciosa/ Enfermedad trasmitible')
    short_comment = fields.Char('Observaciones')
    healed_date = fields.Date('Sanado')
    physician_id = fields.Many2one('medical.patient','Doctor')
    is_allergy = fields.Boolean('Alergias')
    is_infectious = fields.Boolean('Enfermedad infecciosa')
    allergy_type  = fields.Selection([('drug_allergy', 'Alergia a un medicamento'),('food_allergy', 'Alergia a un alimento'),('misc', 'Varios')], 'Tipo de alerigia')
    pregnancy_warning = fields.Boolean('Advertencia de embarazo')
    weeks_of_pregnancy = fields.Integer('Contraido en la semana de embarazo #')
    is_on_treatment = fields.Boolean('Actualmente en tratamiento')
    treatment_description = fields.Char('Descripcion de tratamiento')
    date_start_treatment = fields.Date('Inicio de tratamiento')
    date_stop_treatment = fields.Date('Finaliacion de tratamiento')
    psc_code_id = fields.Many2one('psc.code', 'Codigo')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    