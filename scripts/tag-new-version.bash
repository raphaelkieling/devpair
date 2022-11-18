#!/bin/bash

set -x

# Set next version number
export RELEASE=$1

FINAL_VERSION="${RELEASE:1}"

# Update poetry version
poetry version $FINAL_VERSION

# Push
git add -A
git commit -m "Poetry updated to: $RELEASE"
git push origin main

# Create tags
git tag -a $RELEASE -m "Release $FINAL_VERSION"
git push origin $RELEASE
