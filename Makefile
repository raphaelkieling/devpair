unit:
	python -m pytest

setup:
	python -m pip install -r requirements.txt

local-env:
	APP_ENV=local python setup.py develop

clear-dist:
	rm -Rf dist devpair.egg* build localdevpair.egg*

dist: clear-dist
	python setup.py sdist bdist_wheel

publish-test: dist
	python -m twine upload --repository testpypi --skip-existing dist/*

publish: dist
	python -m twine upload --repository pypi --skip-existing dist/*