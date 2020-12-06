import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-shortlink',
    version='0.0.8',
    packages=['shortlink'],
    description='A simple Django App to hold short links mapped to long urls used in your projects.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Execut3',
    author_email='execut3.binarycodes@gmail.com',
    url='https://github.com/Execut3/django-shortlink',
    license='GPT',
    install_requires=[
        'Django>=2.0',
    ],
    include_package_data=True,
)
