{
    'name': 'Multi-Company Stock Details',
    'summary': 'View product stock quantities across multiple companies from a single product form.',
    'version': '19.0.1.0.0',
    'category': 'Inventory',
    'description': """
Multi-Company Stock Details
===========================

This module adds a dedicated tab on the product form to display stock
quantities across multiple companies.

Main Features
-------------
* View total quantity across all companies.
* Display stock details by company.
* Display warehouse/location for each quantity.
* Access controlled by a dedicated security group.
* Supports multi-company environments.
* Easy-to-use interface integrated into the product form.

Perfect for businesses managing inventory across multiple legal entities.
    """,
    'author': 'Yassir Sheva',
    'maintainer': 'Yassir Sheva',
    'website': 'https://www.linkedin.com/in/yassir203',
    'license': 'LGPL-3',
    'price': 10,
    'currency': 'USD',
    'depends': [
        'base',
        'stock',
    ],

    'data': [
        'security/security.xml',
        'views/product_view.xml',
    ],

    'images': [
        'static/description/banner.png',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
