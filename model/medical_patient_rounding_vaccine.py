# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_rounding_vaccine(models.Model):
    _name = 'medical.patient.rounding.vaccine'
    
    vaccine_id = fields.Many2one('product.product',string="Vacunas",required=True)
    quantity = fields.Integer(string="Cantidad")
    lot_id = fields.Many2one('stock.production.lot',string='Lote',required=True)
    dose = fields.Integer(string="Dosis")
    next_dose_date = fields.Datetime(string="Proxima dosis")
    short_comment = fields.Char(string='Comentario')
    medical_patient_rounding_vaccine_id = fields.Many2one('medical.patient.rounding',string="Vacunas")

