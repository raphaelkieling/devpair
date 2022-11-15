unit:
	python -m pytest

setup:
	python -m pip install -r requirements.txt

clear-dist:
	rm -Rf dist devpair.egg* build localdevpair.egg*

local-env: clear-dist
	APP_ENV=local python setup.py develop

dist: clear-dist
	python setup.py sdist bdist_wheel

publish-test: dist
	python -m twine upload --repository testpypi --skip-existing dist/*

publish: dist
	python -m twine upload --repository pypi --skip-existing dist/*