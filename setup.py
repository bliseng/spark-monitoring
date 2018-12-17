from setuptools import setup

setup(
    name='spark-monitoring',
    version='',
    packages=['examples', 'sparkmonitoring'],
    url='https://bliseng.github.io/spark-monitoring/',
    license='',
    author='Drew J. Sonne',
    author_email='',
    description='',
    install_requires=['requests'],
    extras_requires={'pandas': ['pandas', 'matplotlib']},
    build_requires=['pydoc-markdown'],
)
