[![Build Status](https://travis-ci.com/dmukuna/iReporter.svg?branch=ch-ci-travis-%23162337239)](https://travis-ci.com/dmukuna/iReporter)
[![Coverage Status](https://coveralls.io/repos/github/dmukuna/iReporter/badge.svg?branch=ch-ci-travis-%23162337239)](https://coveralls.io/github/dmukuna/iReporter?branch=ch-ci-travis-%23162337239)

# iReporter

iReporter is a flask RESTful API that enables users to:
- Raise a red-flag
- view a list of red-flags
- view a particular red-flag
- Edit a red-flag's property
- Delete a red-flag record

## Getting Started

1) Clone the repository by doing: `git clone https://github.com/dmukuna/iReporter.git`

2) Create a virtual environment: `virtualenv env`

3) Activate the virtual environment: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows.

4) Install the requirements : `pip install -r requirements.txt`

## Running tests
- Run this command on the terminal:  `pytest`

### Prerequisites

-  Python 3.6.5
-  virtual environment

## Running it on machine
- Create a .env file to store your environment variables: `touch .env`

- In the `.env` file add this lines: `export SECRET=<your-secret-key-here` and `export FLASK_APP="run.py"`
- On terminal do: `source .env`
- Run the application: `flask run`
- The api endpoints can be consumed using postman.

## Endpoints
| Endpoint                                   | FUNCTIONALITY                         |
| ----------------------------------------   |:-------------------------------------:|
| POST /api/v1/red-flags                     | This will create a red-flag           |
| GET  /api/v1/red-flags                     | This will get all red-flags           |
| GET  /api/v1/red-flags/flag_Id             | retrieve a single red-flag by id      |
| PUT  /api/v1/red-flags/flag_Id             | Update a red-flag record              |
| DELETE /api/v1/red-flags/flag_Id           | Delete a red-flag record              |
| PATCH  /api/v1/red-flags/flag_Id/attr      | This will modify a red-flag's property|

## Built With
* [Flask](http://flask.pocoo.org/) -  The web framework used
* [Pip](https://pypi.python.org/pypi/pip) -  Dependency Management
