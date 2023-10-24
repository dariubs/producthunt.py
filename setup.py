from setuptools import setup, find_packages

setup(
    name='producthunt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0,<3.0.0',
        'graphene>=3.0,<4.0'
    ],
    author='Dariush Abbasi',
    author_email='poshtehani@gmail.com',
    description='A Python wrapper on Product Hunt API',
)