# Example of project configuration

## Requirements

* python>=3.4
* virtualenv
* make

## so_parser
A simple module, which uses requests_futures to read tags from stackoverflow API
This module has basic logging set up

## so_server
A simple web application, written in bottle, which is run on nginx and uwsgi.
It has `uwsgi.ini` file with uwsgi settings and `nginx-site` with nginx settings

## tests
Contains unit tests for so_parser with support of `pytest-catchlog`, `requests-mock` and `pytest-mock`
Contains integration tests for so_server with support of `webtest`
Contains end-to-end tests for so_server - deployed to isolated docker container and run against http requests

## Development
`.pylintrc` contains rules for linter
Use `docker-compose.yml` to deploy web server and run web tests on docker
Use `dockerfile.os` to build docker image with Debian and all required dependencies
To install to a fresh environment run: `make`
To list other available commands:`make help`
Consult `Makefile` to understand setup details.
Consult `README-dev.md` to understand basic commands.




