#!/bin/bash

set -x

# Set next version number
export RELEASE=$1

FINAL_VERSION="${RELEASE:1}"

# Create tags
poetry version $FINAL_VERSION
git add -A
git commit --allow-empty -m "Release $FINAL_VERSION"
git tag -a $RELEASE -m "Version $FINAL_VERSION"

# Push
git push origin main
