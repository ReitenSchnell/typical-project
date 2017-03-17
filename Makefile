TESTDIR = tests
MODULE_NAME = so_parser

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
	python -m pytest $(TESTDIR) -v --cov=$(MODULE_NAME)

.PHONY: style
style: environ
	pylint $(MODULE_NAME)

.PHONY: all
all: style coverage


