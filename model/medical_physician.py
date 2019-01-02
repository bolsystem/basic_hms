# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_physician(models.Model):
    _name="medical.physician"
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner','Physician',required=True)
    institution_partner_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string='Institution')
#     speciality_id = fields.Many2one('medical.speciality','Speciality',required=True)
    code = fields.Char('Id')
    info = fields.Text('Extra Info')
