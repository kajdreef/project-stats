# Project-stats

Goal of the project is to create a tool that quickly gives some statistics about the projects I use for research purposes.

## How to install:

- Install the following tools:
    - [scc](https://github.com/boyter/scc/)
    - [git](https://git-scm.com/)

- The tool itself can be installed using: `pip install -e .`

## Plugins:
- [x] Detect build system (limited to: gradle, maven, bazel, and ant).
- [x] Number of contributors
- [x] Line count (maybe use scc or cloc?)
- [ ] Total number of commits
- [ ] Age of project (date last commit - date first commit)
- [ ] Number of test methods