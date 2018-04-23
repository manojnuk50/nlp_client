"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='nlp-utility',  # Required
    version='1.1.0',  # Required
    description='GCP NLP utility functions',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/pypa/sampleproject',  # Optional
    author='Manojkumar vadivel',  # Optional
    author_email='manojkumar.vsj@gmail.com',  # Optional
    keywords='nlp python',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=['google-api-python-client==1.6.6', 'google-cloud==0.32.0'],  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'nlp_client=google_nlp.nlp_client:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
    },
)
