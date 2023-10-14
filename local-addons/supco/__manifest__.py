{
    'name': 'SupCo',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Supreme Court Introduction Letter',
    'depends': ['base'],
    'data': [
        'views/supco_letter_views.xml',
        'views/supco_department_views.xml',
        'views/supco_employee_views.xml',
        'views/supco_menus.xml',
        'views/templates.xml',
        'reports/supco_letter.xml',
        'reports/supco_letter_action.xml',
    ],
    'installable': True,
    'application': True,
}
