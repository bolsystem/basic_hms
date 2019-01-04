# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology_group(models.Model):
    _name = 'medical.pathology.group'
    
    name = fields.Char(string="Nombre",required=True)
    code = fields.Char(string="Codigo")
    desc = fields.Char(string="Descripcion corta",required=True)
    info = fields.Text(string="Informacion detallada")


