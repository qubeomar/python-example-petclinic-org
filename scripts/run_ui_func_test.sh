#!/bin/bash

export PYTHONPATH=/usr/local/lib/python3.5:/usr/local/lib/python3.5/site-packages

python -m petclinic.tests.ui.homepage_menu_tests $1 $2
