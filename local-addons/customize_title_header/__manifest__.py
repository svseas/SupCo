# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Customize Title Header",
    "version": "15.0.1.0.0",
    "sequence": 1,
    "summary": """
        Web Shortcut Customization Shortcut Editable Favicon Editable Shortcut Favicon Setup Title Header Title Browser Title Navigator
    """,
    "description": "Choose your own Title to display on the browser header.",
    "author": "Innoway",
    "maintainer": "Innoway",
    "price": "0.0",
    "currency": "USD",
    "website": "https://innoway-solutions.com",
    "license": "LGPL-3",
    "images": ["static/description/wallpaper.png"],
    "depends": ["web"],
    "data": ["views/title.xml"],
    "assets": {
        "web.assets_backend_prod_only": [
            "customize_title_header/static/src/js/favicon.js",
        ],
    },
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": True,
    "qweb": [],
}
