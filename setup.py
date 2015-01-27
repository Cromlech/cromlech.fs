# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0-crom'

install_requires = [
    'setuptools',
    'zope.interface',
    'zope.schema',
    ]

tests_require = [
    ]

setup(name='cromlech.fs',
      version=version,
      description="A filesystem folder/fole abstraction package for Cromlech",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Cromlech',
      author='The Dolmen Team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://gitweb.dolmen-project.org',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['cromlech'],
      include_package_data=True,
      extras_require={'test': tests_require},
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
