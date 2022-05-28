from setuptools import setup, find_packages

with open('requirements.txt') as f:
    REQUIRED = f.read().split('\n')

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='jeo_services',
    version='0.1.0',
    description='Geo based micro services',
    long_description=readme,
    author='Juan Pablo Salamanca Ramirez',
    author_email='jpsalamarcara@unal.edu.co',
    license=license,
    packages=find_packages(exclude=('test',)),
    install_requires=REQUIRED,
    include_package_data=True
)
