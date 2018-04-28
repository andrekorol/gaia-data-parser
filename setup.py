#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of gaia-data-parser.
#
# gaia-data-parser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gaia-data-parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gaia-data-parser.  If not, see <http://www.gnu.org/licenses/>.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# meta-data
__license__ = 'GNU General Public License (GPL) Version 3'

config = {
    'description': '',
    'author': 'André Rossi Korol',
    'url': 'https://github.com/andrekorol/gaia-data-parser',
    'download_url': 'https://github.com/andrekorol/gaia-data-parser/archive/master.zip',
    'author_email': 'anrobits@yahoo.com.br',
    'version': '0.1',
    'install_requires': [],
    'packages': ['gaia-data-parser'],
    'scripts': ['bin/semanticversion-updater'],
    'name': 'gaia-data-parser',
    'license': __license__
}

setup(**config)
