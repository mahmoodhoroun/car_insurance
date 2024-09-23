{
    'name':'Custom CRM',

    'depends':['base', 'crm'],
    "sequence": 1,
    'installable': True,
    'application': True,
    'data': [
        'security/contact_security.xml',
        'security/ir.model.access.csv',
        'views/car_model_views.xml',
        'views/crm_lead_views.xml',
    ],
}