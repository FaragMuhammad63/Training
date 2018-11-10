from odoo import fields, models, api, exceptions


class Assign(models.TransientModel):
    _name = 'training.assign'

    employee_id = fields.Many2one(comodel_name="res.users",  string="Employee", required=False, )
    course_id = fields.Many2one(comodel_name="training.course", string="Course", required=False, )

    @api.multi
    def assign_course(self):
        self.ensure_one()
        data = self.read()[0]
        name = self.env['training.course'].search([('id', '=', data['course_id'][0])]).name
        employee = self.env['res.users'].search([('id', '=', data['employee_id'][0])]).id
        course = self.env['training.course'].search([('id', '=', data['course_id'][0])]).id
        print course, "***********"

        self.env['training.course.line'].create({
            'name':name,
            'employee_id':employee,
            'course_id':course
        })


