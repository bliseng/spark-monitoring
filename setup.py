from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spark-monitoring',
    version='0.0.3',
    packages=['examples', 'sparkmonitoring'],
    url='https://bliseng.github.io/spark-monitoring/',
    license='LGPL3',
    author='Drew J. Sonne',
    author_email='drew.sonne@gmail.com',
    description='A python library to interact with the Spark History server',
    install_requires=['requests'],
    extras_requires={'pandas': ['pandas', 'matplotlib']},
    build_requires=['sphinx-markdown-builder'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
