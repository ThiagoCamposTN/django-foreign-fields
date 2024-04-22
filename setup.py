import os
import subprocess
from setuptools import find_packages, setup

def get_latest_tag():
    ref = os.getenv("GITHUB_REF")
    if ref:
        return ref.split("/")[-1]
    else:
        return "0.0.0"  # Default version

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-foreign-fields',
    version=get_latest_tag(),
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app with new form fields for handling foreign relationships.',
    long_description=README,
    url='https://github.com/ThiagoCTN/django-foreign-fields/',
    author='Thiago Nascimento',
    author_email='thiagocampostn@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)