<div align="center">
    <img src="./logo.png" width="60px">
</div>

## Dev Pair

[![Python Test](https://github.com/raphaelkieling/pair/actions/workflows/push.yml/badge.svg)](https://github.com/raphaelkieling/pair/actions/workflows/push.yml)

It's a tool to facilitate the pair programming session. Instead of make a lot of `git add, git commit, git push, git pull`, you can make it more quickly only running `devpair start, devpair next`.

## How it works?

**Short version:**

You will work inside a temporary pair branch that in that end all the commits will be squashed to be added to the feature branch.

**Detailed version:**

Under the hood the `devpair start` will take your current branch and create a copy with the same name but with the prefix `pair` 

After make your code changes the `devpair next` will add, commit and push your code using an internal commit message. This step will be more easier to understand checking the [example step by step](#example-of-use)

In the end, we have the `devpair done` that will add, commit, push and delete the branch. Don't worry we will make a squash commit of everything that you did for the current branch.

[![](https://mermaid.ink/img/pako:eNqNkMEKwjAMhl9l5Dzx3rPgA3jtJbb_1uLajpgiMvbu1oOgDGE5fSTfn0AWcsWDDI1Rz8JzsLlr5UpKUbd8Fc4udBmPwwDWKtjlzxzluDv0wwHuVqpuTybIiH-bP6nEMX_rG5N6apOm-faD5d2zpAEJlkxDj4HrpJZsXpvKVcvlmR0ZlYqe6uxZcYo8CicyA093rC_K-3GZ?type=png)](https://mermaid.live/edit#pako:eNqNkMEKwjAMhl9l5Dzx3rPgA3jtJbb_1uLajpgiMvbu1oOgDGE5fSTfn0AWcsWDDI1Rz8JzsLlr5UpKUbd8Fc4udBmPwwDWKtjlzxzluDv0wwHuVqpuTybIiH-bP6nEMX_rG5N6apOm-faD5d2zpAEJlkxDj4HrpJZsXpvKVcvlmR0ZlYqe6uxZcYo8CicyA093rC_K-3GZ)

## Install

```
pip install devpair
```

### Example of use

```bash
# Dev A
main $ devpair start
pair/main $ echo "hello" > welcome.txt
pair/main $ devpair next

# Dev B
main $ devpair start
pair/main $ cat welcome.txt # shows "hello"
pair/main $ echo " world" >> welcome.txt
pair/main $ devpair next

# Dev A again
pair/main $ devpair start
pair/main $ cat welcome.txt # shows "hello world"
pair/main $ echo "!" >> welcome.txt
pair/main $ devpair done

main $ git commit -m "feat: created hello world feature"
main $ git push

# Dev B again
pair/main $ devpair done # just to clear the house. 


# Any Dev
pair/main $ devpair summary # print a summary

Last Dev: 
     dev-a@gmail.com  | 2022-11-16 00:40:00
First Dev: 
     dev-a@gmail.com  | 2022-11-15 17:55:19
Frequence: 
     dev-a@gmail.com         | ▇▇ 2
     dev-b@gmail.com         | ▇ 1
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
