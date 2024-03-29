{
    "name": "supco",
    "version": "1.0",
    "category": "Custom",
    "summary": "Supreme Court Introduction Letter",
    "depends": ["base", "web", "customize_title_header", "log_view"],
    "data": [
        "views/supco_login.xml",
        "views/supco_letter_views.xml",
        "views/supco_department_views.xml",
        "views/supco_employee_views.xml",
        "views/supco_menus.xml",
        "views/supco_404.xml",
        "views/supco_preference.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
        "security/validity_date_rule.xml",
        "views/templates.xml",
        "reports/supco_letter.xml",
        "reports/supco_letter_action.xml",
        "data/data.xml",
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
    "installable": True,
    "application": True,
}
