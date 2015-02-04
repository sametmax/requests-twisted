#!/usr/bin/env python

from setuptools import setup

setup(
    name='requests-twisted',
    version='0.1.2',
    description='Twisted adapter for the requests library.',
    long_description=open('README.rst').read(),
    author='Sam et Max',
    author_email='lesametlemax@gmail.com',
    include_package_data=True,
    py_modules=['requests_twisted'],
    install_requires=['twisted', 'requests'],
    license='Zlib Licence',
    url='https://github.com/sametmax/requests-twisted',
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)
