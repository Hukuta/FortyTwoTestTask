#!/usr/bin/env bash
MANAGE=django-admin.py
SETTINGS=fortytwo_test_task.settings
PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) print_objects_count 2> $(date +"%m_%d_%Y").dat