{
    'name': 'Highlight Current Row',
    'summary': 'Highlight the selected row in all Odoo list views for better visibility.',

    'version': '19.0.1.0.0',
    'category': 'Productivity',

    'description': """
Highlight Current Row
=====================

This module improves the user experience by highlighting the selected row
in all Odoo List Views.

Main Features
-------------
* Automatically highlights the clicked row.
* Works across all standard List Views.
* Lightweight implementation using OWL and CSS.
* No configuration required.
* No database changes.
* Compatible with Community and Enterprise editions.
* Supports Odoo 19.

Benefits
--------
* Easily identify the active row.
* Improve navigation in large datasets.
* Reduce selection mistakes.
* Clean and modern user experience.
    """,

    'author': 'Yassir Sheva',
    'maintainer': 'Yassir Sheva',
    'website': 'https://www.linkedin.com/in/yassir203',
    'license': 'LGPL-3',

    'depends': [
        'web',
    ],

    'assets': {
        'web.assets_backend': [
            'ym_highlight_current_row/static/src/js/highlight.js',
            'ym_highlight_current_row/static/src/css/highlight.css',
        ],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
}