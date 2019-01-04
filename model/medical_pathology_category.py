# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology_category(models.Model):
    _name = 'medical.pathology.category'
    
    name = fields.Char(string="Nombre de categoria",required=True)
    active = fields.Boolean(string="Activa" , default = True)
    parent_id = fields.Many2one('medical.pathology.category', string="Categoria Padre")

