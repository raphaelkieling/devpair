unit:
	poetry run pytest --cov=app

setup:
	python -m pip install -r requirements.txt

build: clear-dist
	poetry build

publish: build
	poetry publish
