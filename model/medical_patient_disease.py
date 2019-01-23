# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from datetime import date,datetime
from odoo import api, fields, models, _


class medical_patient_disease(models.Model):
    _name = "medical.patient.disease"
    _rec_name = 'patient_id'

    pathology_id = fields.Many2one('medical.pathology','Patología', required=True)
    disease_severity =  fields.Selection([('1_mi','Leve'),
                               ('2_mo','Moderada'),
                               ('3_sv','Severa')],'Severidad')
    status =  fields.Selection([('c','Crónica'),
                               ('s','Estatus quo'),
                               ('h','Curado'),
                               ('i','Mejorando'),
                               ('w','Empeorando')],'Estado Patología')
    is_infectious = fields.Boolean('Patología infecciosa')
    is_active = fields.Boolean('Patología activa')
    short_comment = fields.Text('INFORME MÉDICO')
    diagnosis_date = fields.Date('Fecha de Informe')
    healed_date = fields.Date('Fecha de alta')
    age = fields.Integer('Edad cuando fue diagnosticado')
    doctor_id = fields.Many2one('medical.physician','Médico')
    is_allergic = fields.Boolean('Enfermedad alergica')
    allergy_type =  fields.Selection([('da','Alergia a farmaco'),
                               ('fa','Alergia a la comida'),
                               ('ma','Alergias varias'),
                               ('mc','Contraindicaciones varias')],'tipo de alergia')
    pregnancy_warning = fields.Boolean('E/Embarazo')
    week_of_pregnancy = fields.Integer('Contraido en la semana de embarazo #')
    is_on_treatment = fields.Boolean('Actualmente en Trat.')
    treatment_description = fields.Char('Descrip. Trat.')
    date_start_treatment = fields.Date('Inicio Trat.')
    date_stop_treatment = fields.Date('Fecha Alta')
#     medical_procedure_id = fields.Many2one('medical.procedure','Code')
    patient_id = fields.Many2one('medical.patient',string="Paciente")
#     new_born_id = fields.Many2one('medical.newborn',string="Newborn")
    extra_info = fields.Text('Informacion Extra')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: