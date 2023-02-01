# Demo CLI project

With scaffold dependencies:
- PyTest
- Sphinx
- MyPy
- PyType (at this moment global, Python 3.11 is not supported by PyType)
- Flake8 with forks
- Black (alternative: yapf)

And some more...

## How to use the tools?
- use `poetry install` comand for installing all dependencies
- Run tests with `pytest .` command or `poetry run pytest tests/`
- Generate documentation with `sphinx-build -b html source build
` (or start new documentation sources with `sphinx-quickstart` command)
- use command `mypy .` for type correctness checking
- use `flake8 .` command for checking code style and security
- use `black .` command for running automatic code refactoring
- use `yapf --in-place .` for replacing black with something better
- use `make checklist` to run some automated commands together
- it is worth to remember about `pytype` package

Environment created by Poetry. All dependency versions are in `poetry.lock` file. Project configuration along with `black` 
configuration is in the `pyproject.toml` file.