import os
from setuptools import setup

setup(
    name = 'PyDeltaDuck',
    version = '0.0.1',
    description = 'Explore Implementing a DuckPond using Delta Tables using Python.',
    long_description = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')).read(),
    long_description_content_type = 'text/markdown',
    author = 'Giridhar. Dayaneni',
    install_requires = ['virtualenv', 'setuptools', 'pipreqs']
)