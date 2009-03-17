from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='collective.saconnect',
      version=version,
      description="A Plone control panel for SQL Alchemy connection strings",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Jarn AS',
      author_email='info@jarn.com',
      url='https://svn.plone.org/svn/collective/collective.saconnect',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.z3cform',
          'rwproperty',
          'zope.lifecycleevent',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
