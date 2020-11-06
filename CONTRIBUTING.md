# Contributing

## Table of Contents

-   [How to Contribute](#how-to-contribute)
    -   [Style](#style)
    -   [System Requirements](#system-requirements)
    -   [Clone this Repository](#clone-this-repository)
    -   [Git Branching Style](#git-branching-style)
    -   [Git Commit Style](#git-commit-style)
    -   [Testing Changes](#testing-changes)
    -   [Pre-commit webhook](#pre-commit-webhook)
    -   [Submit a Pull Request](#submit-a-pull-request)

## How to Contribute

### Style

-   Enable Python auto-format with [black]
-   Enable Pre commit webhooks with [pre-commit]

### Clone this Repository

To get started, clone this repository. See [GitHub: Cloning a Repository](https://help.github.com/en/articles/cloning-a-repository).

### Git Commit Style

Git commit messages usually come in 2 parts:

-   A subject line (required)
-   A body (optional, but helpful to explain additional detail).

**Style**:

-   Separate the _subject_ from the _body_ with a blank line
-   Limit _subject_ to 50 characters
-   Subject should supply useful information
-   Use sentence case<sup>[1](#footnote-1)</sup> for the _subject_
-   _Do not_ end the _subject_ with a period
-   Use imperative mood<sup>[2](#footnote-2)</sup> for the _subject_
-   Wrap the _body_ at 72 characters
-   Use the _body_ to explain what and _why vs. how_

**Examples**:

```bash
# Bad
# ---
#   - "added" is _not_ in the imperative mood
#   - Subject is wordy and more than 50 characters
#   - Does not use correct casing
#   - Adds a period at the end
added homepage carousel and worked out default config and init scripts.

# Bad
# ---
#   - Subject is too brief and doesn't provide any useful info
#   - Does not use correct casing
fixes

# Other Examples to Avoid
# -----------------------
more fixes
fixed typo
stuff

# Good
# ----
#   - "Add" is in the imperative mood
#   - Subject is concise and informative and is less than 50 characters
#   - Uses correct casing
#   - Does _not_ add period at the end.
Add homepage carousel

# Good
# ----
#   - Follows subject styleguide
#   - A blank line separates subject and body
#   - Body wraps around 72 characters.
Replace GA with GTM

GTM provides several advantages over traditional GA.
All tracking tags can now be managed by the user
without a developer from the GTM console.

```

### Test Changes

Run the Python test suite:

```bash
pytest
```

### Pre-commit webhook
We use pre-commit to:
* Sort imports (with isort)
* Format changed code (with black)
* Check for code with flake8

In order to do this run:
```bash
pre-commit install
```

If you want to call the hooks explicitly before doing a commit you can run

```bash
pre-commit run
```
This will run the hooks on your STAGED files, so make sure they are staged.

Running this for the first time may take 2-4 minutes, so if you want to speed your first commit run it before you need it.

Keep in mind that the commit fails if any of the hooks don't pass.

isort and black fails if they changed the file, so it might be better if you run this command before doing a commit,
otherwise, it's highly probable that it will fail.

On the other hand flake9 will fail if there's something wrong in the code, as an undefined variable, in this case see
the error and fix it in order to make the commit.


### Submit a Pull Request

Once you've added and tested your changes [create a pull request](https://help.github.com/en/articles/creating-a-pull-request).

---

<sup id="footnote-1">1</sup> <small>**Sentence case**: Sentence case is when you only capitalise the first letter of the first word in a heading – like you would in a sentence.</small>

<sup id="footnote-2">2</sup> <small>**Imperative mood**: The imperative mood is a verb form which makes a command or a request. For example: "Empty the bin, John." (the verb is in the imperative mood) versus "John empties the bin." (the verb is not in the imperative mood).</small>

<!-- Links -->
<!-- NOTE: Please keep this list alphabetized. -->

[black]: https://github.com/python/black "Python Black"
[pre-commit]: https://pre-commit.com/ "Pre commit"

<!-- End Links -->
