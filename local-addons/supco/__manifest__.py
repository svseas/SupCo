{
    'name': 'supco',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Supreme Court Introduction Letter',
    'depends': ['base'],
    'data': [
        'views/supco_views.xml',
        'views/supco_menus.xml',
        'reports/supco_letter.xml',
        'reports/supco_letter_action.xml',
    ],
    'assets': {
        'web.report_assets_common': [
          '/custom_font/static/src/scss/custom_font.scss'
        ],
    },
    'installable': True,
    'application': True,
}
