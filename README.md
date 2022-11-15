<div align="center">
    <img src="./logo.png" width="60px">
</div>

## Pair

> The tool is under development.

It's a tool based on [mob](https://mob.sh/). In the end the goal is the same, make the pair programming more easier than make a lot of `git add, git commit, git push, git pull`.

### Why?

I do not agree with the mob principle `no dependencies`. It's good, but it create a lot of code for something that already exist. Making hard to mantain, mainly for new devs that are willing to contribute.

Also i want to explore the integration with anothers tools with a plugin system.

### Example

```sh
# - Dev A
pair start
# Make some code changes
pair next

# - Dev B
pair start
# Receive the Dev A changes and make changes
pair next

# ... and so on until someone make a
pair done
```

### Contributing

Fork and create a branch from `main` with the pattern `feat/my-feature` and make a pull request with your proposal.

### Local env

```sh
# Set the version
pyenv local 3.10.4
# Run all the tests
python -m pytest

# Set the develop
python setup.py develop
# Run the pair
python -m pair ...
```