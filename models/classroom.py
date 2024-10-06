from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Classroom(models.Model):
  _name = 'ad.classroom'
  _description = 'Classroom Information'

  # Campos
  name = fields.Char(string='Nombre', required=True)
  capacity = fields.Integer(string='Capacidad', required=True)
  start_date = fields.Date(string='Fecha Inicio', required=True)
  end_date = fields.Date(string='Fecha Fin', required=True )
  # Campos calculados
  current_students = fields.Integer(compute='_compute_current_students', string='Estudiantes Actuales')
  # Relaciones
  teacher_ids = fields.Many2many('ad.teacher', string='Profesores')
  student_ids = fields.One2many('ad.student', 'classroom_id', string='Estudiantes')
  subject_ids = fields.Many2many('ad.subject', string='Materias')

  #Funciones
  @api.constrains('start_date', 'end_date')
  def _check_date(self): # permite validar las fechas
    for record in self:
        if record.end_date <= record.start_date:
            raise ValidationError("La fecha de fin debe ser mayor que la fecha de inicio.")

  @api.constrains('capacity', 'student_ids')
  def _check_capacity(self): # permite validar que no haya mas estudiantes que la capacidad permitida
    for record in self:
        if len(record.student_ids) > record.capacity:
            raise ValidationError("La cantidad de estudiantes no puede exceder la capacidad del aula.")

  @api.depends('student_ids')
  def _compute_current_students(self): # calcula el numero de estudiantes actuales
    for record in self:
        record.current_students = len(record.student_ids)



