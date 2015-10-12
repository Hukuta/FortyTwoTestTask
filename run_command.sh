#!/usr/bin/env bash
PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=fortytwo_test_task.settings django-admin.py print_objects_count 2> $(date +"%m_%d_%Y").dat