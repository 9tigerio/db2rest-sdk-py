# Summary
A Python client for interacting with a DB2Rest REST API.  DB2Rest instances provide a nocode automatic REST API for databases without the need for code generation or an ORM.

Project repository at https://github.com/9tigerio/db2rest-sdk-py
Official DB2Rest project at https://github.com/9tigerio/db2rest 

# Installation
`python3 -m pip install db2rest`

# Development
## Build
  `python3 -m build`

## Install 
- After building, install using the locally built wheel
 
  `pip install ./dist/db2rest-0.0.1-py3-none-any.whl`

## Test
- Navigate into the top level project folder `db2rest-sdk-py`
- Run `python3 -m pip install --editable .` (take note of the period at end)
- Create tests or Modify existing ones in the `tests` folder.
  - Ensure they are prefixed as `test_*.py` files. Example: `test_RDBMSApi_find_all.py`
- Change directory to the tests folder `cd tests`
- Run all the tests from the project folder with `python3 -m unittest`