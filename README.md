# Gitize

It is a python CLI command that does the followings,
- Creates a poetry project.
- Runs git init.
- Creates a license file.

This tool uses `prj-gen` library and serves as an example to show how to use `prj-gen`.

## Install

### Using poetry
```
poetry add git+https://github.com/kkibria/gitize.git
```

### Using pip
```
pip install gitize@git+https://github.com/kkibria/gitize.git
```

## Running
```
python -m gitize <path>
```

In some systems it can also be executed directly,
```
gitize <path>
```
