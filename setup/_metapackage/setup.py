import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-field-service",
    description="Meta package for oca-field-service Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-fieldservice',
        'odoo12-addon-fieldservice_agreement',
        'odoo12-addon-fieldservice_delivery',
        'odoo12-addon-fieldservice_distribution',
        'odoo12-addon-fieldservice_maintenance',
        'odoo12-addon-fieldservice_repair',
        'odoo12-addon-fieldservice_sale',
        'odoo12-addon-fieldservice_skill',
        'odoo12-addon-fieldservice_stock',
        'odoo12-addon-fieldservice_vehicle',
        'odoo12-addon-fieldservice_vehicle_stock',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
