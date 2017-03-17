PARSER_TESTDIR = tests/so_parser
SERVER_TESTDIR = tests/so_server
TESTDIR = tests
PARSER_MODULE_NAME = so_parser
SERVER_MODULE_NAME = so_server

.PHONY: environ
environ: $(PIP) requirements.txt requirements-dev.txt
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: help
help:
	@echo "make test             # run tests"
	@echo "make coverage         # run tests with coverage report"
	@echo "make style            # check linting with pylint"
	@echo "make all              # check style and coverage"

.PHONY: test
test: environ
	python -m pytest $(TESTDIR) -v

.PHONY: coverage
coverage: environ
	python -m pytest $(PARSER_TESTDIR) -v --cov=$(PARSER_MODULE_NAME)
	python -m pytest $(SERVER_TESTDIR) -v --cov=$(SERVER_MODULE_NAME)

.PHONY: style
style: environ
	pylint $(PARSER_MODULE_NAME)
	pylint $(SERVER_MODULE_NAME)

.PHONY: all
all: style coverage


