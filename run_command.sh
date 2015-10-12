#!/usr/bin/env bash
cd $1
$2 manage.py print_objects_count 2> $(date +"%m_%d_%Y").dat