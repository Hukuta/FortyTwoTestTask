#!/usr/bin/env bash

if [ ! $# == 1 ]; then
  echo "Usage: $0 path_to_your_python_with_django"
  exit
fi

$1 manage.py print_objects_count 2> $(date +"%m_%d_%Y").dat