#!/usr/bin/env python

from setuptools import setup

setup(
    name='openworm-model-dashboard',
    version='0.1',
    description='OpenWorm Model Completion Dashboard',
    author='OpenWorm',
    author_email='info@openworm.org',
    url='https://github.com/openworm/model-completion-dashboard',
    install_requires=('Django==2.0',
                      'djangorestframework==3.7.7',
                      'django-webpack-loader==0.6.0',
                      'PyOpenWorm==0.7.1')
)
