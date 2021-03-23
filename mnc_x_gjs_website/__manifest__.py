{
    'name': 'Website MNC X GJS',
    'description': 'MNC X GJS website in Odoo',
    'category': 'Website',
    'author': 'Sandi Gautama',
    'sequence': 180,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_view.xml',
    ],
    'installable': True,
    'application': True,
}
