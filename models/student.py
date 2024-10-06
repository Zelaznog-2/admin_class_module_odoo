from odoo import models, fields, api


class Student(models.Model):
  _name = 'ad.student'
  _description = 'Student Information'

  # Campos
  name = fields.Char(string='Nombre', required=True)
  last_name = fields.Char(string='Apellido', required=True)
  date_of_birth = fields.Date(string='Fecha de nacimiento', required=True)
  # Relaciones
  classroom_id = fields.Many2one('ad.classroom', string='Aula')
