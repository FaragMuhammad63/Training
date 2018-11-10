# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _inherit = "res.users"

    course_line_ids = fields.One2many(comodel_name="training.course.line", inverse_name="employee_id", string="Courses", )