#!/usr/bin/env python
from setuptools import setup

setup(name='surimisp',
      version='1.0.4',
      description='Python Suricata IOC parser',
      author='Eric Leblond',
      author_email='eleblond@stamus-networks.com',
      url='https://www.stamus-networks.com/',
      scripts=['surimisp'],
      requires=['argparse','pygtail','redis','elasticsearch'],
     )
