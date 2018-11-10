# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'training.course'
    _description = "Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    task_ids = fields.One2many(comodel_name="training.task", inverse_name="course_id", string="Tasks", )


class CourseLine(models.Model):
    _name = 'training.course.line'
    _rec_name = 'name'

    name = fields.Char()
    employee_id = fields.Many2one("res.users", string="", )
    course_id = fields.Many2one(comodel_name="training.course", string="", )
    task_line_ids = fields.One2many("training.task.line", "course_line_id", string="Tasks", required=False, )

    @api.model
    def create(self, values):
        values['name'] = self.env['training.course'].search([('id', '=', values['course_id'])]).name
        res = super(CourseLine, self).create(values)

        if 'task_line_ids' not in values.keys():
            tasks = self.env['training.course'].search([('id', '=', values['course_id'])]).task_ids
            data = []

            for rec in tasks:
                available = False
                if not rec.task_id:
                    available = True
                data.append((0, 0, {
                    'name': rec.name,
                    'course_line_id': res.id,
                    'task_id': rec.id,
                    'pre_task_id': rec.task_id.id,
                    'duration': rec.duration,
                    'is_available': available,
                }))
                values['task_line_ids'] = data

        return super(CourseLine, self).create(values)

    @api.onchange('course_id')
    def onchange_course_id(self):
        tasks = self.course_id.task_ids

        if not tasks:
            return {}

        data = []
        for rec in tasks:
            available = False
            if not rec.task_id:
                available = True
            data.append((0, 0, {
                'name': rec.name,
                'course_line_id': self.id,
                'task_id': rec.id,
                'pre_task_id': rec.task_id.id,
                'duration': rec.duration,
                'is_available': available,
            }))
            self.task_line_ids = data

    # @api.constrains('employee_id', 'course_id')
    # def _check_employee_courses(self):
    #     if len(self.env['training.course.line'].search([('')]))

    # _sql_constraints = [('unique_course_employee', 'UNIQUE(employee_id, course_id)', 'This employee already enrolled in this course before')]