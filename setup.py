from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='producthunt',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0,<3.0.0',
        'graphene>=3.0,<4.0'
    ],
    author='Dariush Abbasi',
    author_email='poshtehani@gmail.com',
    description='A Python wrapper on Product Hunt API',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)