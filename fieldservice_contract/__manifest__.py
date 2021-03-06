# Copyright (C) 2019 - Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service - Contracts',
    'summary': 'Manage FSM Contracts',
    'author': 'Akretion, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/field-service',
    'category': 'Field Service',
    'license': 'AGPL-3',
    'version': '12.0.1.2.0',
    'depends': [
        'product_contract_variable_quantity',
        'fieldservice_sale',
        'fieldservice_sale_recurring',
    ],
    'data': [
        'views/contract.xml',
        'views/contract_line.xml',
        'views/fsm_recurring.xml',
        'views/fsm_order.xml',
        'data/fsm_contract_data.xml',
    ],
    'installable': True,
    'development_status': 'Beta',
    'maintainers': [
        'hparfr',
        'brian10048',
    ],
}
