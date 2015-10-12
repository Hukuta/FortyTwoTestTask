#!/usr/bin/env bash
cd $1
PYTHONPATH=$1
MANAGE=django-admin.py
SETTINGS=fortytwo_test_task.settings

PYTHONPATH=$1 DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) print_objects_count

#$2 manage.py print_objects_count 2> $(date +"%m_%d_%Y").dat