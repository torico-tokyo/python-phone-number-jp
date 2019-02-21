# -*- coding: utf-8 -*-

from __future__ import unicode_literals

menu = [
    ('cancel',
     ""),
    ('test',
     ["./setup.py test"]),
    ('flake8',
     "flake8 phone_number_jp"),
    ('upload pypi',
     "./setup.py sdist; twine upload --skip-existing dist/*"),
]
