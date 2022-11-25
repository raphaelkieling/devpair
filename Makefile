unit:
	poetry run pytest --cov=app --cov-report term-missing

setup:
	poetry install && poetry run pre-commit install

build: clear-dist
	poetry build

publish: build
	poetry publish

local:
	poetry install && poetry shell

coverage:
	poetry run coverage run --source=app -m pytest tests/
