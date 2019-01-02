# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 

class medical_patient(models.Model):
    
    _name = 'medical.patient'
    _rec_name = 'patient_id'

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id

    @api.multi
    def print_report(self):
        return self.env.ref('basic_hms.report_print_patient_card').report_action(self)

    @api.depends('date_of_birth')
    def onchange_age(self):
        if self.date_of_birth:
            dt = self.date_of_birth
            d1 = datetime.strptime(dt, "%Y-%m-%d").date()
            d2 = datetime.today()
            rd = relativedelta(d2, d1)
            self.age = str(rd.years) + "a" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
        else:
            self.age = "No hay fecha de Nacimiento!!"

    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Paciente", required= True)
    name = fields.Char(string='ID', readonly=True)
    last_name = fields.Char('Apellidos')
    date_of_birth = fields.Date(string="Fecha de Nacimiento")
    sex = fields.Selection([('m', 'Masculino'),('f', 'Femenino')], string ="Sexo")
    age = fields.Char(compute=onchange_age,string="Edad del Paciente",store=True)
    critical_info = fields.Text(string="Informacion critica del paciente")
    photo = fields.Binary(string="Foto")
    blood_type = fields.Selection([('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O')], string ="Tipo de sangre")
    rh = fields.Selection([('-+', '+'),('--', '-')], string ="Rh")
#     medical_ethnicity_id = fields.Many2one('medical.ethnicity',string="Ethnic Group")
    marital_status = fields.Selection([('s','Soltero'),('m','Casado'),('w','Viudo'),('d','Divorciado'),('x','Separado')],string='Estado marital')
#     family_code_id = fields.Many2one('medical.family_code',string="Family")
    deceased = fields.Boolean(string='Fallecido')
    date_of_death = fields.Datetime(string="Fecha de muerte")
    cause_of_death = fields.Char(string='Cause de la muerte')
    receivable = fields.Float(string="Cuenta x cobrar", readonly=True)
    current_insurance_id = fields.Many2one('medical.insurance',string="Seguro")
    partner_address_id = fields.Many2one('res.partner', string="Direccion", )
    primary_care_physician_id = fields.Many2one('medical.physician', string="Medico Principal")
    patient_status = fields.Char(string="Estado de hospitalizacion",readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease','patient_id')
    patient_psc_ids = fields.One2many('medical.patient.psc','patient_id')
#     evaluation_ids = fields.One2many('medical.patient.evaluation','medical_patient_id',string="Evalution")
    excercise = fields.Boolean(string='Ejercios')
    excercise_minutes_day = fields.Integer(string="Minutos/Dia")
    sleep_hours = fields.Integer(string="Horas de sueño")
    sleep_during_daytime = fields.Boolean(string="Dormir durante el día")
    number_of_meals = fields.Integer(string="Comidas por día")
    coffee = fields.Boolean('Cafe')
    coffee_cups = fields.Integer(string='Tazas por día')
    eats_alone = fields.Boolean(string="Eats alone")
    soft_drinks = fields.Boolean(string="Soft drinks(sugar)")
    salt = fields.Boolean(string="Salt")
    diet = fields.Boolean(string=" Currently on a diet ")
    diet_info = fields.Integer(string=' Diet info ')
    general_info = fields.Text(string="Info")
    lifestyle_info = fields.Text('Información de estilo de vida')
    smoking = fields.Boolean(string="Fumar")
    smoking_number = fields.Integer(string="Cigarros por día")
    ex_smoker = fields.Boolean(string="Ex-fumador")
    second_hand_smoker = fields.Boolean(string="Fumador pasivo")
    age_start_smoking = fields.Integer(string="Age started to smoke")
    age_quit_smoking = fields.Integer(string="Age of quitting")
    drug_usage = fields.Boolean(string='Drug Habits')
    drug_iv = fields.Boolean(string='IV drug user')
    ex_drug_addict = fields.Boolean(string='Ex drug addict')
    age_start_drugs = fields.Integer(string='Age started drugs')
    age_quit_drugs = fields.Integer(string="Age quit drugs")
    alcohol = fields.Boolean(string="Drinks Alcohol")
    ex_alcohol = fields.Boolean(string="Ex alcoholic")
    age_start_drinking = fields.Integer(string="Age started to drink")
    age_quit_drinking = fields.Integer(string="Age quit drinking")
    alcohol_beer_number = fields.Integer(string="Beer / day")
    alcohol_wine_number = fields.Integer(string="Wine / day")
    alcohol_liquor_number = fields.Integer(string="Liquor / day")
    cage_ids = fields.One2many('medical.patient.cage','patient_id')
#     drugs_ids = fields.Many2many('medical.drugs_recreational', string="Drugs")
    sex_oral = fields.Selection([('0','Ninguno'),
                                 ('1','Activo'),
                                 ('2','Pasivo'),
                                 ('3','Natural')],string='Sexo oral')
    sex_anal = fields.Selection([('0','Ninguno'),
                                 ('1','Activo'),
                                 ('2','Pasivo'),
                                 ('3','Natural')],string='Sexo anal')
    prostitute = fields.Boolean(string='Prostituta')
    sex_with_prostitutes = fields.Boolean(string=' Sexo con prostitutas ')
    sexual_preferences = fields.Selection([
            ('h', 'Heterosexual'),
            ('g', 'Homosexual'),
            ('b', 'Bisexual'),
            ('t', 'Transexual'),
        ], 'Sexual Orientation', sort=False)
    sexual_practices = fields.Selection([
            ('s', 'Segura / Proteccion sex'),
            ('r', 'Riesgosa / Sin proteccion sex'),
        ], 'Practicas sexuales', sort=False)
    sexual_partners = fields.Selection([
            ('m', 'Monogamo'),
            ('t', 'Poligamo'),
        ], 'Pareja sexual', sort=False)
    sexual_partners_number = fields.Integer('Número de parejas sexuales')
    first_sexual_encounter = fields.Integer('Edad de su primer relacion sexual')
    anticonceptive = fields.Selection([
            ('0', 'Niguna'),
            ('1', 'Pildora / Minipildora'),
            ('2', 'Condon Masculino'),
            ('3', 'Vasetomia'),
            ('4', 'Estirilizacion femenina'),
            ('5', 'Dispositivo intra-uterino'),
            ('6', 'Metodo de retirada'),
            ('7', 'Control de los dias'),
            ('8', 'Inyeccion anticonseptiva'),
            ('9', 'Parche de piel'),
            ('10', 'Condon Femenino'),
        ], 'Método anticonseptivo', sort=False)
    sexuality_info = fields.Text('Extra Information')
    motorcycle_rider = fields.Boolean('Maneja moto', help="El paciente maneja moto")
    helmet = fields.Boolean('Usa casco', help="El paciente usa el casco adecuado")
    traffic_laws = fields.Boolean('Obeys Traffic Laws', help="Check if the patient is a safe driver")
    car_revision = fields.Boolean('Car Revision', help="Maintain the vehicle. Do periodical checks - tires,breaks ...")
    car_seat_belt = fields.Boolean('Seat belt', help="Safety measures when driving : safety belt")
    car_child_safety = fields.Boolean('Car Child Safety', help="Safety measures when driving : child seats, proper seat belting, not seating on the front seat, ....")
    home_safety = fields.Boolean('Home safety', help="Keep safety measures for kids in the klitchen, correct storage of chemicals, ...")
    fertile = fields.Boolean('Fertile')
    menarche = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausal')
    menopause = fields.Integer('Menopause age')
    menstrual_history_ids = fields.One2many('medical.patient.menstrual.history','patient_id')
    breast_self_examination = fields.Boolean('Breast self-examination')
    mammography = fields.Boolean('Mammography')
    pap_test = fields.Boolean('PAP test')
    last_pap_test = fields.Date('Last PAP test')
    colposcopy = fields.Boolean('Colposcopy')
    mammography_history_ids = fields.One2many('medical.patient.mammography.history','patient_id')
    pap_history_ids = fields.One2many('medical.patient.pap.history','patient_id')
    colposcopy_history_ids = fields.One2many('medical.patient.colposcopy.history','patient_id')
    pregnancies = fields.Integer('Pregnancies')
    premature = fields.Integer('Premature')
    stillbirths = fields.Integer('Stillbirths')
    abortions = fields.Integer('Abortions')
    pregnancy_history_ids = fields.One2many('medical.patient.pregnency','patient_id')
#     genetic_risks_ids = fields.Many2many('medical.genetic.risk',string="Genetic Risks")
    family_history_ids = fields.Many2many('medical.family.disease',string="Family Disease Lines")
    perinatal_ids = fields.Many2many('medical.preinatal')
    ex_alcoholic = fields.Boolean('Ex alcoholic')
    currently_pregnant = fields.Boolean('Currently Pregnant')
#     surgery_ids = fields.One2many('medical.surgery','patient_id')
    born_alive = fields.Integer('Born Alive')
    gpa = fields.Char('GPA')
    works_at_home = fields.Boolean('Works At Home')
    colposcopy_last = fields.Date('Last colposcopy')
    mammography_last = fields.Date('Last mammography')
    ses = fields.Selection([
            (None, ''),
            ('0', 'Baja'),
            ('1', 'Baja-media'),
            ('2', 'Media'),
            ('3', 'Media-alta'),
            ('4', 'Alta'),
        ], 'Clasesocial', help="CS - Clase social", sort=False)
    education = fields.Selection([('o','Ninguno'),('1','Incompleta - estudios primarios'),
                                  ('2','Escuela primaria'),
                                  ('3','Incompleta - Escuela secundaria'),
                                  ('4','Escuela secundaria'),
                                  ('5','Universitario')],string='Nivel de educacion')
    housing = fields.Selection([
            (None, ''),
            ('0', 'Choza, condicion sanitaria deficiente'),
            ('1', 'Pequeña, apretado pero con buenas condiciones'),
            ('2', 'Confortable y con buena condicion sanitaria'),
            ('3', 'Excelente y condicion sanitarias buenas'),
            ('4', 'Lujosa y Condiciones sanitarias excelentes'),
        ], 'Condiciones de vivienda', help="Vivienda y Condiciones de vida sanitaria", sort=False)
    works = fields.Boolean('Trabajo')
    hours_outside = fields.Integer('Hours outside home', help="Number of hours a day the patient spend outside the house")
    hostile_area = fields.Boolean('Hostile Area')
    notes = fields.Text(string="Iformacion extra")
    sewers = fields.Boolean('Sanitary Sewers')
    water = fields.Boolean('Running Water')
    trash = fields.Boolean('Trash recollection')
    electricity = fields.Boolean('Electrical supply')
    gas = fields.Boolean('Gas supply')
    telephone = fields.Boolean('Telephone')
    television = fields.Boolean('Television')
    internet = fields.Boolean('Internet')
    single_parent= fields.Boolean('Single parent family')
    domestic_violence = fields.Boolean('Domestic violence')
    working_children = fields.Boolean('Working children')
    teenage_pregnancy = fields.Boolean('Teenage pregnancy')
    sexual_abuse = fields.Boolean('Sexual abuse')
    drug_addiction = fields.Boolean('Drug addiction')
    school_withdrawal = fields.Boolean('School withdrawal')
    prison_past = fields.Boolean('Has been in prison')
    prison_current = fields.Boolean('Is currently in prison')
    relative_in_prison = fields.Boolean('Relative in prison', help="Check if someone from the nuclear family - parents sibblings  is or has been in prison")
    fam_apgar_help = fields.Selection([
            (None, ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Help from family',
            help="Is the patient satisfied with the level of help coming from the family when there is a problem ?", sort=False)
    fam_apgar_discussion = fields.Selection([
            (None, ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Problems discussion',
            help="Is the patient satisfied with the level talking over the problems as family ?", sort=False)
    fam_apgar_decisions = fields.Selection([
            (None, ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Decision making',
            help="Is the patient satisfied with the level of making important decisions as a group ?", sort=False)
    fam_apgar_timesharing = fields.Selection([
            (None, ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Time sharing',
            help="Is the patient satisfied with the level of time that they spend together ?", sort=False)
    fam_apgar_affection = fields.Selection([
            (None, ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Family affection',
            help="Is the patient satisfied with the level of affection coming from the family ?", sort=False)
    fam_apgar_score = fields.Integer('Score', help="Total Family APGAR 7 - 10 : Functional Family 4 - 6  : Some level of disfunction \n"
                                          "0 - 3  : Severe disfunctional family \n")
    lab_test_ids = fields.One2many('medical.patient.lab.test','patient_id')
    fertile = fields.Boolean('Fertile')
    menarche_age  = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausal')
    pap_test_last = fields.Date('Last PAP Test')
    colposcopy = fields.Boolean('Colpscopy')
    gravida = fields.Integer('Pregnancies')
    medical_vaccination_ids = fields.One2many('medical.vaccination','medical_patient_vaccines_id')
    medical_appointments_ids = fields.One2many('medical.appointment','patient_id',string='Appointments')
    lastname = fields.Char('Last Name')
    report_date = fields.Date('Date',default = fields.Datetime.now)
    medication_ids = fields.One2many('medical.patient.medication1','medical_patient_medication_id')
    #medications = fields.One2many('medical.patient.medication','medical_patient_medication_id',string='Medication')
    deaths_2nd_week = fields.Integer('Deceased after 2nd week')
    deaths_1st_week = fields.Integer('Deceased after 1st week')
    full_term = fields.Integer('Full Term')
#     occupation_id = fields.Many2one('medical.occupation','Occupation')
    ses_notes = fields.Text('Notes')

    @api.model
    def create(self,val):
        appointment = self._context.get('appointment_id')
        res_partner_obj = self.env['res.partner']
        if appointment:
            val_1 = {'name': self.env['res.partner'].browse(val['patient_id']).name}
            patient= res_partner_obj.create(val_1)
            val.update({'patient_id': patient.id})
        if val.get('date_of_birth'):
            dt = val.get('date_of_birth')
            d1 = datetime.strptime(dt, "%Y-%m-%d").date()
            d2 = datetime.today()
            rd = relativedelta(d2, d1)
            age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            val.update({'age':age} )
        '''if val['patient_id']:
            val.update({
                        'name':self.env['res.partner'].browse(val['patient_id']).name,
                       })'''
        patient_id  = self.env['ir.sequence'].next_by_code('medical.patient')
        if patient_id:
            val.update({
                        'name':patient_id,
                       })        
        result = super(medical_patient, self).create(val)
        return result


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
