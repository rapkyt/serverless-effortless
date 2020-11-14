# serverless-effortless

## Table of Contents

-   [Install](#install)
-   [Usage](#usage)
-   [Maintainers](#maintainers)
-   [Contributing](#contributing)

## Install
### System Requirements

<!-- NOTE: Keep this list alphabetized. -->

-   [Black]
-   [Git]
-   [Node] & [Npm]
-   [NVM]
-   [Poetry]
-   [Pyenv]
-   [Python]
-   [Serverless]
-   [Virtualenv]

### Setup - Python
```bash
# STEP 1:
# NOTE: `pyenv local` Should output -> 3.6.10
$ pyenv local

# STEP 2: Create and activate local virtualenv.
$ virtualenv .venv --python=python3.6

# STEP 3: Install local Python packages.
$ poetry install
```


## Usage



### Deploy

**NOTE**: This would upload all your code (in `serverless` folder) to lambda functions.

```bash
# Configure your AWS Profile
$ serverless config credentials --provider aws --key {{key}} --secret {{secret}} --profile {{profile_name}}

# Copy the .env.dist file and fill the values
$ cp config/.env.dist config/.env.dev
$ cp config/.env.dist config/.env.prod


# NOTE: Deploy
$ serverless deploy --stage {{stage}} --env {{stage}}

# For instance, to deploy on dev: 
$ serverless deploy --stage dev --env dev
```


## Maintainers

-   [Cristian Mora](https://github.com/rapkyt/)

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted.

<!-- Links -->
<!-- Please keep this list alphabetized. -->

[black]: "https://github.com/python/black" "Black"
[git]: "https://git-scm.com/" "Git"
[node]: "https://nodejs.org/en/download/" "Node"
[npm]: "https://docs.npmjs.com/" "NPM"
[nvm]: "https://github.com/creationix/nvm" "NVM"
[poetry]: "https://poetry.eustace.io/docs/" "Poetry"
[pyenv]: "https://github.com/pyenv/pyenv" "Pyenv"
[python]: "https://www.python.org/" "Python"
[serverless]: "https://serverless.com/" "Serverless"
[virtualenv]: "https://virtualenv.pypa.io/en/stable/" "Virtualenv"

<!-- End Links -->
