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
    procedencia = fields.Char( string="Lugar/Procedencia", help="Ej. Montero, Warnes. San Ignacio, Etc.")
    partner_address_id = fields.Many2one('res.partner', string="Direccion", )
    primary_care_physician_id = fields.Many2one('medical.physician', string="Medico Principal")
    patient_status = fields.Char(string="Estado de hospitalizacion",readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease','patient_id')
    patient_psc_ids = fields.One2many('medical.patient.psc','patient_id')
#     evaluation_ids = fields.One2many('medical.patient.evaluation','medical_patient_id',string="Evalution")
    excercise = fields.Boolean(string='Ejercios')
    excercise_minutes_day = fields.Integer(string="Minutos/Dia")
    sleep_hours = fields.Integer(string="Horas que duerme")
    sleep_during_daytime = fields.Boolean(string="Duerme durante el día")
    number_of_meals = fields.Integer(string="Comidas por día")
    coffee = fields.Boolean('Cafe')
    coffee_cups = fields.Integer(string='Tazas por día')
    eats_alone = fields.Boolean(string="Come solo")
    soft_drinks = fields.Boolean(string="Bebidas sin alcohol (azúcar)")
    salt = fields.Boolean(string="Sal")
    diet = fields.Boolean(string=" Actualmente hace dieta ")
    diet_info = fields.Integer(string=' Nro. dietas')
    general_info = fields.Text(string="Info")
    lifestyle_info = fields.Text('Información de estilo de vida')
    smoking = fields.Boolean(string="Fumador")
    smoking_number = fields.Integer(string="Cigarros por día")
    ex_smoker = fields.Boolean(string="Ex-fumador")
    second_hand_smoker = fields.Boolean(string="Fumador pasivo")
    age_start_smoking = fields.Integer(string="Edad que empezo a fumar")
    age_quit_smoking = fields.Integer(string="Edad en que dejo de fumar")
    drug_usage = fields.Boolean(string='Consume drogas')
    drug_iv = fields.Boolean(string='Consume drogas IV')
    ex_drug_addict = fields.Boolean(string='Ex drogadicto')
    age_start_drugs = fields.Integer(string='Edad que empezo a consumir drogas')
    age_quit_drugs = fields.Integer(string="Edad en la que dejo de usar drogas")
    alcohol = fields.Boolean(string="Toma alcohol")
    ex_alcohol = fields.Boolean(string="Ex alcoholico")
    age_start_drinking = fields.Integer(string="Edad en la que empezo a consumir alcohol")
    age_quit_drinking = fields.Integer(string="Edad en que dejo de consumir alcohol")
    alcohol_beer_number = fields.Integer(string="Cerveza / semana")
    alcohol_wine_number = fields.Integer(string="Vino / semana")
    alcohol_liquor_number = fields.Integer(string="Licor / semana")
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
    traffic_laws = fields.Boolean('Maneja seguro', help="Es el paciente un conductor seguro")
    car_revision = fields.Boolean('Revision del auto', help="Mantto. vehiculo. Hace un mantenimiento periodico.")
    car_seat_belt = fields.Boolean('Cinturon de seguridad', help="Usa cinturon de seguridad")
    car_child_safety = fields.Boolean('Seguridad para niños', help="El auto tiene medidas de seguridad para niños : asiento para niños, ect....")
    home_safety = fields.Boolean('Seguridad en el hogar', help="Toma medidas de seguridad para los niños en el hogar, lugar correcto para medicamentos, Etc..")
    fertile = fields.Boolean('Fertil')
    menarche = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausica')
    menopause = fields.Integer('Edad menopausica')
    menstrual_history_ids = fields.One2many('medical.patient.menstrual.history','patient_id')
    breast_self_examination = fields.Boolean('Autoexamen semanal')
    mammography = fields.Boolean('Mamografia')
    pap_test = fields.Boolean('PAP Prueba')
    last_pap_test = fields.Date('Utima prueba PAP')
    colposcopy = fields.Boolean('Coloscopia')
    mammography_history_ids = fields.One2many('medical.patient.mammography.history','patient_id')
    pap_history_ids = fields.One2many('medical.patient.pap.history','patient_id')
    colposcopy_history_ids = fields.One2many('medical.patient.colposcopy.history','patient_id')
    pregnancies = fields.Integer('Embarazos')
    premature = fields.Integer('Prematuro')
    stillbirths = fields.Integer('Aborto')
    abortions = fields.Integer('Aborto probocado')
    pregnancy_history_ids = fields.One2many('medical.patient.pregnency','patient_id')
#     genetic_risks_ids = fields.Many2many('medical.genetic.risk',string="Genetic Risks")
    family_history_ids = fields.Many2many('medical.family.disease',string="Enfermedades Familiares")
    perinatal_ids = fields.Many2many('medical.preinatal')
    ex_alcoholic = fields.Boolean('Ex alcoholico')
    currently_pregnant = fields.Boolean('Actualmente embarazada')
#     surgery_ids = fields.One2many('medical.surgery','patient_id')
    born_alive = fields.Integer('Nacidos vivos')
    gpa = fields.Char('GPA')
    works_at_home = fields.Boolean('Trabaja en casa')
    colposcopy_last = fields.Date('Última colposcopia')
    mammography_last = fields.Date('Ultima mamografia')
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
    hours_outside = fields.Integer('Horas fuera de casa', help="Numero de horas que el paciente esta fuera de casa")
    hostile_area = fields.Boolean('Horario hostil')
    notes = fields.Text(string="Iformacion extra")
    sewers = fields.Boolean('Alcantarillas sanitarias')
    water = fields.Boolean('Aguas sobrantes')
    trash = fields.Boolean('Basureros')
    electricity = fields.Boolean('Suministro electrico')
    gas = fields.Boolean('Gas domiciliario')
    telephone = fields.Boolean('Telefono')
    television = fields.Boolean('Television')
    internet = fields.Boolean('Internet')
    single_parent= fields.Boolean('Familia monoparental')
    domestic_violence = fields.Boolean('Violencia domestica')
    working_children = fields.Boolean('Trabajo en niño')
    teenage_pregnancy = fields.Boolean('Embarazo en la adolecencia ')
    sexual_abuse = fields.Boolean('Abuso sexual')
    drug_addiction = fields.Boolean('Addcion a las drogas')
    school_withdrawal = fields.Boolean('Dejo la escuela')
    prison_past = fields.Boolean('Ha estado en la cárcel')
    prison_current = fields.Boolean('Esta Actualmente en prison')
    relative_in_prison = fields.Boolean('Libertad condicional', help="Esta en libertad condicional")
    fam_apgar_help = fields.Selection([
            (None, ''),
            ('0', 'Ninguno'),
            ('1', 'Moderado'),
            ('2', 'Muy bien'),
        ], 'Ayuda de la Familia',
            help="Esta el paciente satisfecho con la ayuda que recibe de su familia ?", sort=False)
    fam_apgar_discussion = fields.Selection([
            (None, ''),
            ('0', 'Ninguna'),
            ('1', 'Moderado'),
            ('2', 'Muy bien'),
        ], 'Discucion problemas',
            help="¿Está el paciente satisfecho con el nivel de problemas que tiene su familia ?", sort=False)
    fam_apgar_decisions = fields.Selection([
            (None, ''),
            ('0', 'Ninguna'),
            ('1', 'Moderado'),
            ('2', 'Muy bien'),
        ], 'Toma de desiciones',
            help="Esta el paciente satisfecho con su nivel de toma de desciones en su grupo/familia ?", sort=False)
    fam_apgar_timesharing = fields.Selection([
            (None, ''),
            ('0', 'Ninguna'),
            ('1', 'Moderado'),
            ('2', 'Muy bien'),
        ], 'Tiempo compartido',
            help="Esta el paciente satisfecho con el timpo quecomparte en familia ?", sort=False)
    fam_apgar_affection = fields.Selection([
            (None, ''),
            ('0', 'Ninguna'),
            ('1', 'Moderado'),
            ('2', 'Muy bien'),
        ], 'Afecto de la familia',
            help="¿Está el paciente satisfecho con el nivel de afecto que viene de la familia ?", sort=False)
    fam_apgar_score = fields.Integer('Pujtaje', help="Total Famlia APGAR 7 - 10 : Famlia Funcional 4 - 6  : Nivel bajo de disfunción \n"
                                          "0 - 3  : Familia disfuncional severa \n")
    lab_test_ids = fields.One2many('medical.patient.lab.test','patient_id')
    fertile = fields.Boolean('Fertilidad')
    menarche_age  = fields.Integer('Edad menopausica')
    menopausal = fields.Boolean('Menopausica')
    pap_test_last = fields.Date('Ultimo test PAP')
    colposcopy = fields.Boolean('Coloscopia')
    gravida = fields.Integer('Embarazos')
    medical_vaccination_ids = fields.One2many('medical.vaccination','medical_patient_vaccines_id')
    medical_appointments_ids = fields.One2many('medical.appointment','patient_id',string='Consultas')
    lastname = fields.Char('Apellidos')
    report_date = fields.Date('Fecha',default = fields.Datetime.now)
    medication_ids = fields.One2many('medical.patient.medication1','medical_patient_medication_id')
    #medications = fields.One2many('medical.patient.medication','medical_patient_medication_id',string='Medication')
    deaths_2nd_week = fields.Integer('Fallecido después de la 2da. semana')
    deaths_1st_week = fields.Integer('Fallecido después de la 1ra. semana')
    full_term = fields.Integer('Termino')
#     occupation_id = fields.Many2one('medical.occupation','Occupation')
    ses_notes = fields.Text('Notas')

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
