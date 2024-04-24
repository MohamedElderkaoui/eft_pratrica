#!/bin/bash

# Function to display error message and exit
display_error() {
    echo "Error: $1" >&2
    exit 1
}

# Run Django system checks
system_check_output=$(python manage.py check 2>&1)

# Check if there are any errors
if [[ $system_check_output == *"ERRORS:"* ]]; then
    # Display error message and exit
    display_error "Django system check identified issues:\n$system_check_output"
fi

# Get installed apps
installed_apps=$(python manage.py diffsettings | grep '^INSTALLED_APPS' | awk '{print $3}' | tr -d ',' | tr -d '\\')

# Iterate over installed apps and generate SQL scripts
for app in $installed_apps; do
    # Run sqlmigrate command for each app
    python manage.py sqlmigrate --database default "$app" zero || display_error "Failed to generate SQL script for app: $app"
done

echo "SQL scripts generated successfully."
