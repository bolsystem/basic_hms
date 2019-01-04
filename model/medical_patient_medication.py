# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_medication(models.Model):
    _name = 'medical.patient.medication'

    medicament = fields.Many2one('medical.medicament',string='Medicamento',required=True)
    medical_patient_medication_id1 = fields.Many2one('medical.patient',string='Medicacion')
    is_active = fields.Boolean(string='Active', default = True)
    start_treatment = fields.Datetime(string='Inicio de tratamiento',required=True)
    course_completed = fields.Boolean(string="Tratamiento completado")
    doctor_physician_id = fields.Many2one('medical.physician',string='Medico')
    indication = fields.Many2one('medical.pathology',string='Indicacion')
    end_treatment = fields.Datetime(string='Fin del tratamiento',required=True)
    discontinued = fields.Boolean(string='Descontinuado')
#     form = fields.Many2one('medical.drug.form',string='Form')
    route = fields.Many2one('medical.drug.route',string=" Via de administracion ")
    dose = fields.Float(string='Dosis')
    qty = fields.Integer(string='X')
    dose_unit = fields.Many2one('medical.dose.unit',string='Unidad de la dosis')
    duration = fields.Integer(string="Duracion de tratamiento")
    duration_period = fields.Selection([('minutes','Minutos'),
                                        ('hours','Horas'),
                                        ('days','Dias'),
                                        ('months','Meses'),
                                        ('years','Años'),
                                        ('indefine','Indefinio')],string='Periodo de tratamiento')
    common_dosage = fields.Many2one('medical.medication.dosage',string='Frecuencia')
    admin_times = fields.Char(string='Horas de administracion')
    frequency = fields.Integer(string='Frecuencia')
    frequency_unit = fields.Selection([('seconds','Segundos'),
                                       ('minutes','Minutos'),
                                       ('hours','Horas'),
                                       ('days','Dias'),
                                       ('weeks','Semanas'),
                                       ('wr','Cuando sea requerido')],string='Unidad')
    notes =fields.Text(string='Notas')
    medical_patient_medication_id = fields.Many2one('medical.patient','Paciente')
#     new_born_id =  fields.Many2one('medical.newborn', 'New Born')
