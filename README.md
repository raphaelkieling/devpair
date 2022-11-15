<div align="center">
    <img src="./logo.png" width="60px">
</div>

## Pair

🖊️ The tool is under development.

It's a tool based on [mob](https://mob.sh/). In the end the goal is the same, make the pair programming more easier than make a lot of `git add, git commit, git push, git pull` during a pair session.


## Install

Working to let you install through pip. If you really want to use it, feel free to clone and run the `make local-env` that will allow will to run `pythom -m pair ...`

### Example of use

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

if you have any doubt

```
pair --help
```

### Recommendation

- Before the pair programming
    - define the end of the session. How many time do you want pair?
    - define the break time.


### Contributing

Fork, create a branch from `main` with the pattern `feat/my-feature` and make a pull request with your proposal.

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
