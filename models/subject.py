from odoo import models, fields, api


class Subject(models.Model):
  _name = 'ad.subject'
  _description = 'Subject Information'

  # Campos
  name = fields.Char(string='Nombre', required=True)
  code = fields.Char(string='Código', required=True)
  credit_hours = fields.Integer(string='Crédito de horas', required=True)
  description = fields.Char(string='Descripción', required=True)
  # Relaciones
  classroom_ids = fields.Many2many('ad.classroom', string='Aula')