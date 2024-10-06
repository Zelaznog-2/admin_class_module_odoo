from odoo import models, fields, api

class Teacher(models.Model):
  _name = 'ad.teacher'
  _description = 'Teacher Information'

  # Campos
  name = fields.Char(string='Nombre', required=True)
  last_name = fields.Char(string='Apellido', required=True)
  specialty = fields.Char(string='Especialidad', required=True)
  # Relaciones
  classroom_ids = fields.Many2many('ad.classroom', string='Aula')
