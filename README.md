<div align="center">
    <img src="https://illustrations.popsy.co/amber/communication.svg" width="200px">
</div>

## Dev Pair

<small>Illustration by: [popsy](https://popsy.co/)</small>

[![Python Test](https://github.com/raphaelkieling/pair/actions/workflows/push.yml/badge.svg)](https://github.com/raphaelkieling/pair/actions/workflows/push.yml)
![PyPI Version](https://img.shields.io/pypi/v/devpair)
![Python Version](https://img.shields.io/pypi/pyversions/devpair)

It's a tool to facilitate the remote pair programming session. Instead of make a lot of `git add, git commit, git push, git pull`, you can make it more quickly only running `devpair start <timer optional>` to start coding and `devpair next` to send the code to another person.

Very useful for teams that like to make pair sessions often. If you never was a driver or a navigator feel free to read [here](https://martinfowler.com/articles/on-pair-programming.html) to have a context.

## Install

```
pip install devpair
```

## Commands

- `devpair start <time in minutes optional>` Start a new session inside the current branch.
- `devpair next` Save everything and send to the next person.
- `devpair done` Finish and put all the work in the original branch.
- `devpair summary` Show a simple resume of commit counts and last developer.
- `devpair cow` It's cow.
- `devpair timer <time in minutes>` Create a simple timer for any purposal.
- `devpair --help` I like to have a help some times.

> We recommend to create some alias if you want, like: `dvs` to run `devpair start`, `dvn` to run `devpair next` and `dvd` to run `devpair done`.

## Example of use

```bash
# Dev A
main $ devpair start 10 # Will start the new branch with a 10 minutes timer
pair/main $ echo "hello" > welcome.txt
pair/main $ devpair next

# Dev B
main $ devpair start
pair/main $ cat welcome.txt # shows "hello"
pair/main $ echo " world" >> welcome.txt
pair/main $ devpair next

# Dev A
pair/main $ devpair start
pair/main $ cat welcome.txt # shows "hello world"
pair/main $ echo "!" >> welcome.txt
pair/main $ devpair done

main $ git commit -m "feat: created hello world feature"
main $ git push

# Dev B
pair/main $ devpair done # just to come back to the original branch
main
```

## How it works internally?

You will work inside a temporary pair branch that in the end all the commits will be squashed to be added to the feature branch.

<details>
    <summary>More details!</summary>

Ok ok! Under the hood the `devpair start` will take your current branch and create a copy with the same name but with the prefix `pair`

After make your code changes the `devpair next` will add, commit and push your code using an internal commit message. This step will be more easier to understand checking the [example step by step](#example-of-use)

In the end, we have the `devpair done` that will add, commit, push and delete the branch. Don't worry we will make a squash commit of everything that you did for the current branch.

[![](https://mermaid.ink/img/pako:eNqNkMEKwjAMhl9l5Dzx3rPgA3jtJbb_1uLajpgiMvbu1oOgDGE5fSTfn0AWcsWDDI1Rz8JzsLlr5UpKUbd8Fc4udBmPwwDWKtjlzxzluDv0wwHuVqpuTybIiH-bP6nEMX_rG5N6apOm-faD5d2zpAEJlkxDj4HrpJZsXpvKVcvlmR0ZlYqe6uxZcYo8CicyA093rC_K-3GZ?type=png)](https://mermaid.live/edit#pako:eNqNkMEKwjAMhl9l5Dzx3rPgA3jtJbb_1uLajpgiMvbu1oOgDGE5fSTfn0AWcsWDDI1Rz8JzsLlr5UpKUbd8Fc4udBmPwwDWKtjlzxzluDv0wwHuVqpuTybIiH-bP6nEMX_rG5N6apOm-faD5d2zpAEJlkxDj4HrpJZsXpvKVcvlmR0ZlYqe6uxZcYo8CicyA093rC_K-3GZ)

</details>

## Recommendations

- Before the pair programming
  - Define the end of the session. How many time do you want pair?
  - Define the break time.
- Use a `timer`, maybe `devpair` timer or any other one, the important thing is to keep the pair rotation:
  - `devpair start <time in minutes>`
  - https://cuckoo.team/
  - https://double-trouble.wielo.co/
  - http://mobtimer.zoeetrope.com/
  - ANY other mobile app, web tool, smartwatch app, pomodoro timer and so on.
- The `driver` need to share the screen avoiding to use tools like `vscode live share`, even they are good it can create some hard moments that you want to show the browser or create a quickly diagram. The preference is that the `driver` ever need to share the screen.
- Antipatterns: https://tuple.app/pair-programming-guide/antipatterns

## Contributing

Fork, create a branch from `main` with the pattern `feat/my-feature` and make a pull request with your proposal.

## Local env

We are using [poetry](https://python-poetry.org/) and [pyenv](https://github.com/pyenv/pyenv) to manage all the python versions and dependencies.

```sh
# Install all the dependencies
poetry install
# Install the pre-commit
poetry run pre-commit install
# Set the version of the `.python-version`
pyenv local
# Run all the tests
make unit
```

## Publishing

```sh
sh ./scripts/tag-new-version.bash v0.0.0
```
