""" setup for hopsapp """
from setuptools import setup

setup(
    name='hopsapp',
    packages=['hopsapp'],
    include_package_data=True,
    install_requires=[
        'flask', 'Flask-SQLAlchemy', 'flask-login', 'psycopg2'
    ],
)
