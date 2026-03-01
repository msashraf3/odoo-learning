from odoo import models, fields

class Student(models.Model):
    _name = 'custom.student'
    _description = 'Student Record'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
