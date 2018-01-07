# pyspark-template


Example PySpark project with standard configuration for:
- code style and analysis [flake8, pylint, PyCharm]
- static vulnerability analysis [bandit]
- unit tests [unittest]
- test coverage [coverage]
- documentation [sphinx]

## Prerequisites
1. `$ pip3 install tox`
2. Install PyCharm
3. Start a new project
4. Start a new virtualenv in PyCharm based on Python3 under `File;Settings...;Project;Project Interpreter` and add `tox` and `pyspark`.

## Usage
You can either copy the files in this template and rename as needed, or use it as an example to create your own files.
1. In your project add your own 'pyspark_script.py'.
2. Add unittests in a `tests/` directory
3. Add a `setup.py`
4. Run `Tools;Sphinx Quickstart`
5. Add a `tox.ini`
6. Run tox.ini

