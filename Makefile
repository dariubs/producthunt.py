.PHONY: all build upload local

all: build 

local:
	- pip install .

build:
	- python setup.py sdist bdist_wheel

upload:
	- twine upload dist/*
