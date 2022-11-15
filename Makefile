unit:
	python -m pytest

setup:
	python -m pip install -r requirements.txt

local-env:
	python setup.py develop