.PHONY: clean-pyc clean-build docs clean

test:
	python manage.py test tests -d -s

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "release - package and upload a release"

clean: clean-pyc clean-test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage

lint:
	flake8
	
run:
	python manage.py runserver

restart:
	uwsgi --stop config/blog.pid || $(make) uwsgi --ini config/uwsgi.ini
