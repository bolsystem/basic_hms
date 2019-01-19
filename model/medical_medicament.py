# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_medicament(models.Model):
  
    _name = 'medical.medicament'
    _rec_name = 'product_id'

    @api.multi
    @api.depends('product_id')
    def onchange_product(self):
        for each in self:
            if each:
                self.qty_available = self.product_id.qty_available
                self.price = self.product_id.lst_price
            else:
                self.qty_available = 0
                self.price = 0.0

    product_id  = fields.Many2one('product.product', 'Nombre')
    therapeutic_action = fields.Char('Efecto terapeutico', help = 'Accion terapeutica')
    price = fields.Float(compute=onchange_product,string='Precio',store=True)
#     category_id = fields.Many2one('medicament.category', 'Category')
    qty_available = fields.Integer(compute=onchange_product,string='Cantidad disponible',store=True)
    indications = fields.Text('Indicaciones')
    active_component = fields.Char(string="Componente activo")
    presentation = fields.Text('Presentacion')
    composition = fields.Text('Composicion')
    dosage = fields.Text('Introducciones de dosis')
    pregnancy = fields.Text('Embarazo')
    overdosage = fields.Text('Sobredosis')
    pregnancy_warning = fields.Boolean('Advertencia de Embarazo')
    pregnancy_category = fields.Selection([('a','A'),('b','B'), ('c','C'), ('d', 'D'), ('x', 'X'), ('n','N')], help = """"** FDA Categorias de embarazo ***CATEGORIA A :Los estudios en humanos adecuados y bien controlados no han demostrado un riesgo para el feto en el primer trimestre del embarazo (y no hay evidencia de riesgo en los trimestres posteriores) CATEGORÍA B: Los estudios de reproducción en animales han fallado para demostrar un riesgo para el feto y no hay estudios adecuados y bien controlados en mujeres embarazadas O Los estudios en animales han mostrado un efecto adverso, pero los estudios adecuados y bien controlados en mujeres embarazadas no han podido Demostrar un riesgo para el feto en cualquier trimestre.

CATEGORIA C : Los estudios de reproducción en animales han mostrado un efecto adverso en el feto y no existen estudios adecuados y bien controlados en humanos, pero los beneficios potenciales pueden justificar el uso del medicamento en mujeres embarazadas a pesar de los riesgos potenciales. 

 CATEGORIA D : Existe evidencia positiva de riesgo fetal humano basado en datos de reacciones adversas de la experiencia de investigación o mercadotecnia o estudios en humanos, pero los beneficios potenciales pueden justificar el uso del medicamento en mujeres embarazadas a pesar de los riesgos potenciales.

CATEGORIA X : Los estudios en animales o humanos han demostrado anormalidades fetales y / o hay evidencia positiva de riesgo fetal humano basado en datos de reacciones adversas de investigación o experiencia en mercadeo, y los riesgos involucrados en el uso del medicamento en mujeres embarazadas claramente superan los beneficios potenciales.

CATEGORIA N : Aún no clasificado""")

    adverse_reaction = fields.Text('Reacion adversa')
    storage = fields.Text('Condicion de almacenamiento')
    notes = fields.Text('Informacion extra')

