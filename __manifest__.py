# -*- coding: utf-8 -*-
{
    'name': "training",

    'summary': """
    Training/Courses  """,

    'description': """
        This module helps managers to assign courses for their employee
        and make managers and employees can keep track the progress of these courses
    """,

    'author': "Farag Muhammad",
    'website': "https://www.linkedin.com/in/farag-muhammad-648776123",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Apps',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', ],

    'application': True,

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/task.xml',
        'views/course.xml',
        'views/employee.xml',
        'wizards/assign.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
