# User Store
Create an APP that stores user data
- Data is composed of first name, last name, address (stree, city, state and zip)
- The app should create the following User types (Parent, Child) The child cannot have an address and Must belong to a parent
- App should have API to:
	- Delete user data
	- Create user data
	- Update user data
- Data can be saved in a file or a DB (which ever is easy)
- Readme file describing how to install/run the application
- The project has to provide a mechanism that tests the application to guarrantee that it works properly


## Prerequisites
- Python 3.8
- Pip
- MongoDB v3.6.8


## install with pipenv
- install pipenv
```bash
$ sudo -H pip3 install -U pipenv
```
- clone the repo & cd into it
- install dependencies
```bash
$ pipenv install
```
- Copy & rename .env.example file to .env
- Set the database credentials inside .env
- run the app
```bash
$ pipenv run gunicorn -b 0.0.0.0:5000 --access-logfile - --reload "app:create_app()"
```
- run tests
```bash
$ pipenv run pytest tests/
```
- run test coverage
```bash
$ pipenv run pytest --cov-report term-missing --cov
```
- run linting
```bash
$ pipenv run flake8 .
```


## in case
- generate requirements.txt
```bash
$ pipenv lock -r > requirements.txt
```

## [API documentation](https://documenter.getpostman.com/view/7833390/T1LLF8m4?version=latest)

