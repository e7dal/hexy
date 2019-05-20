.PHONY: clean-pyc clean-build docs clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "upload_to_pypi - upload a release"
	@echo "version - upDATE version"
	@echo "dist - package"


clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 hexy
	# flake8 hexy tests

test:
	#python setup.py test
	echo "hexy has built in examples, which are basic input output tests:)"
	hexy examples -a | sh


coverage:
	coverage run --source hexy -m behave
	coverage report -m
	coverage html
	open htmlcov/index.html


version:
	echo `date +%Y.%m.%d` >VERSION.txt
	sed -i "s/^version =.*/version = \"`date +%Y.%m.%d`\"/" hexy/metadata.py

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py bdist_wheel
	pip install ./dist/hexy-*-py2.py3-none-any.whl

#upload_to_testpypi: clean dist
#	twine upload dist/* -r testpypi
#	echo "please checkout https://testpypi.python.org/pypi/hexy/"
#	echo "for testing: first install the requirements from pypi"
#	echo "pip install -r requirements.txt"
#	echo "pip install  hexy --index https://testpypi.python.org/pypi --upgrade"
#	echo "looking good? continue with make upload_to_pypi"



upload_to_pypi:
	twine upload dist/*
	echo "please checkout https://pypi.python.org/pypi/hexy/"
	echo "for testing:"
	echo "pipsi install  hexy --upgrade"
	echo "pip install  hexy --upgrade"

