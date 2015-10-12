PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$1 $2 print_objects_count #2> $(date +"%m_%d_%Y").dat
