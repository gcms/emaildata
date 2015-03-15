from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='emaildata',
      version=version,
      description="Python package for extracting metadata, text, html and attachements from email messages.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='email rfc822',
      author='Karel Antonio Verdecia Ortiz',
      author_email='kverdecia@gmail.com',
      url='',
      license='LPGL3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
