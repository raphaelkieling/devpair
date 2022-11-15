<div align="center">
    <img src="./logo.png" width="60px">
</div>

## Dev Pair

[![Python Test](https://github.com/raphaelkieling/pair/actions/workflows/push.yml/badge.svg)](https://github.com/raphaelkieling/pair/actions/workflows/push.yml)

🖊️ The tool is under development.

It's a tool based on [mob](https://mob.sh/). In the end the goal is the same, make the pair programming more easier than make a lot of `git add, git commit, git push, git pull` during a pair session.


## Install

For now it's only possible to download the version to test.

```
pip install devpair
```

### Example of use

```sh
# - Dev A
devpair start
# Make some code changes
devpair next

# - Dev B
devpair start
# Receive the Dev A changes and make changes
devpair next

# ... and so on until someone make a
devpair done
```

if you have any doubt

```
devpair --help
```

### Recommendations

- Before the pair programming
    - Define the end of the session. How many time do you want pair?
    - Define the break time.
- Use a `timer` like. Ordered by preference, for some cases a mobile timer is enough.
    - https://cuckoo.team/
    - https://double-trouble.wielo.co/
    - http://mobtimer.zoeetrope.com/
- The `driver` need to share the screen avoiding to use tools like `vscode live share`, even they are good it can create some hard moments that you want to show the browser or create a quickly diagram. The preference is that the `driver` ever need to share the screen.
- Antipatterns: https://tuple.app/pair-programming-guide/antipatterns


### Contributing

Fork, create a branch from `main` with the pattern `feat/my-feature` and make a pull request with your proposal.

### Local env

```sh
# Set the version
pyenv local 3.10.4
# Run all the tests
python -m pytest

# Set the develop
make local-env
# Run the devpair
python -m localdevpair ...
```

### Publishing

```sh
# it's using twine $HOME/.pypirc [testpypi]
make publish-test

# it's using twine $HOME/.pypirc [pypi]
make publish
```
