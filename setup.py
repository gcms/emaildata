# -*- coding: utf-8 -*-
"""
This file is part of the emailcontent package
Copyrighted by Karel Vedecia Ortiz <kverdecia@gmail.com>
License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
"""
__author__ = "Karel Antonio Verdecia Ortiz"
__contact__ = "kverdecia@gmail.com"


from setuptools import setup, find_packages
import sys, os


version = '0.1'


setup(name='emaildata',
    version=version,
    description="Python package for extracting metadata, text, html and attachements from email messages.",
    long_description="""\
""",
    classifiers=[
        "Topic :: Communications :: Email",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
    ],
    keywords='email rfc822',
    author='Karel Antonio Verdecia Ortiz',
    author_email='kverdecia@gmail.com',
    url='',
    license='LPGL3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'charset>=1.0.1',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
