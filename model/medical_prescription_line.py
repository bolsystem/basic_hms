# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_prescription_line(models.Model):
    _name = "medical.prescription.line"

    name = fields.Many2one('medical.prescription.order','Prescripcion ID')
    medicament_id = fields.Many2one('medical.medicament','Medicamento')
    indication = fields.Text('Rp/')
    allow_substitution = fields.Boolean('Permitir sustitcion')
    form = fields.Char('Formula')
    prnt = fields.Boolean('Imprimir')
    route = fields.Char('Via de administración')
    end_treatement  = fields.Datetime('Via de administración')
    dose = fields.Float('Dosis')
    dose_unit_id = fields.Many2one('medical.dose.unit', 'Unidad/Dosis')
    qty = fields.Integer('Cantidad')
    medication_dosage_id = fields.Many2one('medical.medication.dosage','Frecuencia')
    admin_times = fields.Char('Admin Horas', size = 128)
    frequency = fields.Integer('Frecuencia')
    frequency_unit = fields.Selection([('seconds','Segundos'),('minutes','Minutos'),('hours','horas'),('days','Dias'),('weeks','Semanas'),('wr','Cuando requerido')], 'Unidad')
    duration = fields.Integer('Duracion de tratamiento')
    duration_period = fields.Selection([('minutes','Minutos'),('hours','horas'),('days','Dias'),('months','Meses'),('years','Años'),('indefine','Indefinido')],'Tratamiento periodico')
    quantity = fields.Integer('Cantidad')
    review = fields.Datetime('Revision')
    refills = fields.Integer('Recargas#')
    short_comment = fields.Text('Nota de la prescripcion', size=128 )
    end_treatment = fields.Datetime('Fin de tratamiento')
    start_treatment = fields.Datetime('Inicio de tratamiento')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
