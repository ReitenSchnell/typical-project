ENV = env
FOO = $(ENV)/bin
TESTDIR = tests
MODULE_NAME = so_client

$(FOO):
	virtualenv $(ENV)

.PHONY: help
help:
	@echo "make test             # run tests"
	@echo "make coverage         # run tests with coverage report"
	@echo "make style            # check linting with pylint"

.PHONY: environ
environ: $(PIP) requirements.txt requirements-dev.txt
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: test
test: environ
	python -m pytest $(TESTDIR) -v

.PHONY: coverage
coverage: environ
	python -m pytest $(TESTDIR) -v --cov=$(MODULE_NAME)

.PHONY: style
style: environ
	pylint $(MODULE_NAME)


