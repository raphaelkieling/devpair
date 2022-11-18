#!/bin/bash

set -x

# Set next version number
RELEASE=$1

FINAL_VERSION="${RELEASE:1}"

# Update poetry version
poetry version $FINAL_VERSION

# Push
git add -A
git commit -m "Poetry updated to: $RELEASE"
git push origin main

# Create tags
git commit --allow-empty -m "Release $RELEASE"
git tag -a $RELEASE -m "Version $RELEASE"
git push origin $RELEASE
