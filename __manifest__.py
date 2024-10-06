{
    'name': "admin class module odoo",
    'version': '1.0',
    'sequence': 1,

    'description': """
        Módulo CRM para la gestión de clases...
    """,

    'author': "Carlos Gonzalez",

    'category': 'Education',
    'license': 'LGPL-3',

    'depends': ['base'],
    'demo': ['demo/demo.xml'],
    'data': [
        'security/ir.model.access.csv',
        'views/menus_view.xml',
        'views/classroom_view.xml',
        'views/teacher_view.xml',
        'views/student_view.xml',
        'views/subject_view.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}