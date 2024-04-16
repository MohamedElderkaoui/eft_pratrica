#!/bin/bash

# Get a list of all installed apps in the Django project
APPS=$(python manage.py diffsettings | grep '^INSTALLED_APPS' | awk '{print $3}' | tr -d ',' | tr -d '\\')

# Loop through each app and run the sqlmigrate command
for APP in $APPS
do
    python manage.py sqlmigrate $APP zero
done