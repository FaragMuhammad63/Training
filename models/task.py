# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class Task(models.Model):
    _name = 'training.task'
    _description = "Courses"

    name = fields.Char(string="Title", required=True)
    course_id = fields.Many2one("training.course", string="Course", required=True, )
    duration = fields.Integer(string="Duration(days)", )
    task_id = fields.Many2one(comodel_name="training.task", string="Task Required", )

    @api.onchange('course_id')
    def _get_tasks(self):
        res = {}
        res['domain'] = {'task_id':[('course_id', '=', self.course_id.id)]}
        return res


class TaskLine(models.Model):
    _name = 'training.task.line'

    name = fields.Char(string="Title" )
    duration = fields.Integer(string="Duration(days)", )
    task_id = fields.Many2one("training.task", string="Task", )
    pre_task_id = fields.Many2one("training.task", string="Task Required", )
    course_line_id = fields.Many2one("training.course.line", string="", )
    start = fields.Date(string="Start")
    end = fields.Date(string="End",)
    is_available = fields.Boolean(string="Available", )
    state = fields.Selection(string="", selection=[
        ('waiting', 'Waiting'),
        ('on_progress', 'On Progerss'),
        ('done', 'Done'),
        ('completed', 'Completed'),
    ], default='waiting', )

    def started(self):
        if not self.is_available:
            raise exceptions.Warning("please, finish task : "+self.pre_task_id.name+" before starting this task")
        today = datetime.today()
        self.write({'state': 'on_progress',
                    'start': today.strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                    'end': (today+timedelta(days=self.duration)).strftime(DEFAULT_SERVER_DATETIME_FORMAT)})

    def finished(self):
            self.write({'state': 'done'})

    def completed(self):
            self.write({'state': 'completed'})

            depended_tasks = self.env['training.task.line'].search([('pre_task_id.id', '=', self.task_id.id)])

            for task in depended_tasks:
                task.write({'is_available': True})
                print task.is_available

