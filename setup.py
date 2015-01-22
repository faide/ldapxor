from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='ldapxor',
      version=version,
      description="Rewrite ldap content on the fly",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ldap proxy',
      author='Florent Aide',
      author_email='florent.aide@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'ldaptor',
          'pyopenssl',
          'service_identity',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
