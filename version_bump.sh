#!/bin/bash

# File containing the version number
VERSION_FILE=setup.py

# Collect the current version
CURRENT_VERSION=$(cat $VERSION_FILE | grep version= | grep -o -e "[0-9]\+\.[0-9]\+\.[0-9]\+")
# Create the next version number
NEXT_MINOR=$(expr 1 + $( echo $CURRENT_VERSION | cut -d. -f3))
NEXT_VERSION=$(echo $CURRENT_VERSION | cut -d. -f1,2).$NEXT_MINOR

# Replace the numbers 
sed s/$CURRENT_VERSION/$NEXT_VERSION/ -i $VERSION_FILE
