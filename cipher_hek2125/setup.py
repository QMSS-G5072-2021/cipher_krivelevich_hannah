#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Hannah Krivelevich",
    author_email='hannahkrivelevich@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="HW07 Cookiecutter Practice.",
    entry_points={
        'console_scripts': [
            'cipher_hek2125=cipher_hek2125.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cipher_hek2125',
    name='cipher_hek2125',
    packages=find_packages(include=['cipher_hek2125', 'cipher_hek2125.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/HannahKrivelevich/cipher_hek2125',
    version='0.1.0',
    zip_safe=False,
)
