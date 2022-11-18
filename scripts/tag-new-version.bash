# Set next version number
export RELEASE=$1

# Create tags
poetry version $1
git add -A
git commit --allow-empty -m "Release $RELEASE"
git tag -a $RELEASE -m "Version $RELEASE"

# Push
git push origin main
