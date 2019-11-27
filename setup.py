#!/usr/bin/env python3
#
#   Copyright 2016 Gogo, LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Lavatory installer"""

from setuptools import find_packages, setup
import os

with open('requirements.txt', 'rt') as reqs_file:
    REQUIREMENTS = reqs_file.readlines()

base_path = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(base_path, 'version')

version = os.getenv('PACKAGE_VERSION')
if version:
    with open(version_file, 'w') as f:
        f.write(version.strip())
else:
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            version = f.read().strip()
    else:
        raise RuntimeError('Version could not be determined')

if not version:
    raise RuntimeError('version value is ' + str(version))

data_files = [('', ['version'])]

setup(
    name='lavatory',
    description='Run retention policies against Artifactory repositories',
    long_description=open('README.rst').read(),
    author='Gogo DevOps',
    author_email='ps-devops-tooling@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=REQUIREMENTS,
    include_package_data=True,
    keywords="gogo infrastructure python artifactory jfrog",
    url='https://github.com/gogoair/lavatory',
    download_url='https://github.com/gogoair/lavatory',
    platforms=['OS Independent'],
    license='Apache License (2.0)',
    version=version,
    data_files=data_files,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'lavatory=lavatory.__main__:root'
        ]
    },
)
