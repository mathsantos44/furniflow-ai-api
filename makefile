PYTHONPATH := $(shell pwd)

ifeq ($(shell which docker-compose | grep "docker-compose"),)
	COMMAND := docker compose
else
	COMMAND := docker-compose
endif

build:
	DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker build -t furniflow-ai-api .

run: clean
	uvicorn "src.api.server:app" --host "0.0.0.0" --ws "none" --port "8000"

install:
	@poetry install --no-root

linter: clean format
	@poetry run ruff check . --fix && poetry run black --check .

format:
	@poetry run black .

test: clean
	@poetry run -vvv coverage run -vvv -m pytest && poetry run coverage report -m

test-report: test
	@poetry run coverage html || true

up:
	$(shell $(COMMAND) up -d)

down:
	$(shell $(COMMAND) down)


clean:
	@find . | grep -E '.pyc|.pyo|pycache' | xargs rm -rf
	@find . | grep -E '.pyc|.pyo|pycache|pytest_cache' | xargs rm -rf
	@rm -rf ./htmlcov
	@rm -rf ./pycache
	@rm -rf ./pycache
	@rm -rf ./.pytest_cache
	@rm -rf ./.mypy_cache
	@find . -name 'unit_test.db' -exec rm -r -f {} +
	@find . -name '.coverage' -exec rm -r -f {} +

migrate:
	@poetry run alembic -c ./alembic.ini upgrade head

revision:
	@poetry run alembic revision --autogenerate -m "${COMMENT}"

downgrade:
	@poetry run alembic -c ./alembic.ini downgrade -1