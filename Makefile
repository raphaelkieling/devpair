unit:
	poetry run pytest --cov=app

setup:
	python -m pip install -r requirements.txt

clear-dist:
	rm -Rf dist devpair.egg* build localdevpair.egg*

local-env: clear-dist
	APP_ENV=local python setup.py develop

build: clear-dist
	poetry build

publish: build
	poetry publish