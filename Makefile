unit:
	poetry run pytest --cov=app

setup:
	poetry install && poetry run pre-commit install

build: clear-dist
	poetry build

publish: build
	poetry publish

coverage:
	poetry run coverage run --source=app -m pytest tests/
