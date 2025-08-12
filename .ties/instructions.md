# Instructions

## General Information

This python (3.13) repo uses the astral.sh stack along other CLIs:
1. `devcontainer` - environment isolation
2. `pre-commit` - triggers all of the following CLIs
3. `uv` - venv and CLIs management
4. `ruff` - format and lint
5. `ty` - type checking
6. `pytest` - testing
7. `tox` - tests automation
8. `typos` - spell checking
9. `pip-audit` - dependency security
10. `trivy` - general security
11. `claude` - for an objective AI review
12. `lintok` - file size linter
13. `ties` - file-to-file sync with transformations
14. `yamlfmt` - yaml format and lint
15. `biomejs` - json format and lint
16. `rumdl` - markdown format and lint
17. `lychee` - broken link detection
18. `taplo` - general toml format and lint
19. `pyproject-fmt` - pyproject.toml format and lint
20. `tox-toml-fmt` - tox.toml format and lint

## Git

Commit changes with a `--signoff`.
Commit messages must follow the pattern
`<type>: <sentence>\n[<details>]\n\nAssisted-by: <name-of-code-assistant>`,
where the `<type>` is `feat` or `fix`, the `<sentence>` is no more than 60
characters and the `<details>` are optional.  

## Pre-Commit

`pre-commit` is configured to run all CLIs.  
To run, simply:

```shell
pre-commit
```

With no additional options.  
Before editing anything, **ALWAYS** start with `pre-commit`.  
**NEVER** run a CLI directly before `pre-commit` first.  
Running a CLI directly is a last resort.  

## Edit Attempts

Each sequence of edits and code generation without
`pre-commit` is an Edit Attempt.  
Edit Attempts should be atomic, focused and encapsulated.  
After any Edit Attempt:  
- `git add` all changes
- `pre-commit`
- a summary line: `Attempt #<attempt index>: <status>`  
  where `<status>` is `SUCCESS` or `FAILED`

## Tasks

Each Task is a sequence of Edit Attempts.  
A Task with a single `SUCCESS` is considered `DONE`.  
When a Task is `DONE`, move on to the next Task.  
After 3 `FAILED` Edit Attempts, the Task is considered `STUCK`.  
After any Task:  
- `git commit` your changes
- a summary line: `<task>: <status> after <amount> attempts`  
  where `<status>` is `DONE` or `STUCK`
- `CHANGELOG.md` update if needed

## Goals

A Goal is a testable valuable feature.  
When working on a Goal you must plan Tasks that will
eventually lead you to the Goal completion.  
Tasks must include testing the feature.  
Tasks may be changed, `CANCELED` or added when needed.  
When all Tasks are `DONE` the Goal is `COMPLETED`
You should address the user only if:
1. A Goal was `COMPLETED`
2. You are `STUCK`

After any `COMPLETED` Goal:
- `git push` your changes
- consicely summarize the process
