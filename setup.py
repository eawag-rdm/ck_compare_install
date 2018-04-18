# _*_ coding: utf-8 _*_

from setuptools import setup, find_packages
setup(
    name = 'compare_install',
    version = '0.1',
    packages = find_packages(),
    install_requires = ['docopt>=0.6.2', 'ckanapi>=4.1'],
    author = 'Harald von Waldow',
    author_email = 'harald.vonwaldow@eawag.ch',
    description = ("Compares set of modules loaded in two CKAN instances on"
                   " two different machines. Useful to compare deployment- "
                   " with development environment. Also compares the git"
                   " revison of plugins that are loaded by both apps."
                   ),
    license = " GNU AFFERO GENERAL PUBLIC LICENSE",
    keywords = 'CKAN development',
    entry_points = {
        'console_scripts':
        ['compare_install=ck_compare_install.compare_install:main']
    }
)
