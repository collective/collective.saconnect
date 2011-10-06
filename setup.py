from setuptools import setup, find_packages
import os

version = '1.4'

setup(name='collective.saconnect',
      version=version,
      description="A Plone control panel for SQL Alchemy connection strings",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Jarn AS',
      author_email='info@jarn.com',
      url='http://pypi.python.org/pypi/collective.saconnect',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.z3cform',
          'rwproperty',
          'zope.lifecycleevent',
      ],
      )
