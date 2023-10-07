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
    "assets": {
        "web.assets_backend": [
            "supco/static/src/fonts/scss/fonts.scss",
        ],
        "web.assets_frontend": [
            "supco/static/src/fonts/scss/fonts.scss",
        ],
        "web.report_assets_common": [
            "supco/static/src/fonts/scss/fonts.scss",
        ],
    },
    'installable': True,
    'application': True,
}
