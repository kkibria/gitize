# Gitize

It is a python CLI tool that does the followings,
- Creates a poetry project.
- Runs git init.
- Creates a license file.

This tool uses [`prj-gen`](https://github.com/kkibria/prj-gen) library and
serves as an example to show how to use `prj-gen`.

## Install
`gitize` requires `poetry` and `git` installed in your system and added to
`path` already. Recommended way is to install `gitize` globally and you will
have to install in administrative mode.

### Using poetry
```
poetry add git+https://github.com/kkibria/gitize.git
```

### Using pip
```
pip install gitize@git+https://github.com/kkibria/gitize.git
```

Without the administrative privilege, you can install it in a virtual
environment as well.

## Running
It can be executed directly from command line,
```
gitize <path>
```

You can also run this as a python module,
```
python -m gitize <path>
```
