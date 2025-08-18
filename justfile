set positional-arguments

alias p := pre-commit
alias pa := pre-commit-all
alias t := test
alias b := bump

# pre-commit the current changes
pre-commit:
  git add .
  pre-commit $@

# pre-commit all repo files
pre-commit-all:
  pre-commit run --all

# test all python versions and coverage the latest python version
test:
  tox --parallel $@

# bump the version (major/minor/patch/alpha)
bump:
  hatch version $@
