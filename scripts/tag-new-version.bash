#!/bin/bash

# Show all commands
set -x
# Stop if have any error
set -e

if [[ $1 =~ ^v[0-9]+(\.[0-9]+){2,3}$ ]];
then
    echo Yes
else
    echo "You must follow the format vX.X.X"
    exit 1
fi

# Keep update
git pull origin main

# Set next version number
RELEASE=$1

FINAL_VERSION="${RELEASE:1}"

# Update poetry version
poetry version $FINAL_VERSION

# Push
git add -A
git commit -m "Poetry updated to: $RELEASE"

# Create tags
git tag -a $RELEASE -m "Version $RELEASE"
git push origin $RELEASE

git push origin main
