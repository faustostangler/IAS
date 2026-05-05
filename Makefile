.PHONY: help up down restart logs ps test lint format build shell

help:
	@echo "IAS (Intelligent Audio Scriber) Commands:"
	@echo "  up      - Start all services in background"
	@echo "  down    - Stop and remove all containers"
	@echo "  restart - Restart all services"
	@echo "  logs    - Show logs from all containers"
	@echo "  ps      - Show running containers"
	@echo "  test    - Run tests inside a container"
	@echo "  lint    - Run ruff check and mypy"
	@echo "  format  - Run ruff format"
	@echo "  build   - Build or rebuild services"
	@echo "  shell   - Open a shell in the api container"

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

ps:
	docker compose ps

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run mypy src

format:
	uv run ruff format .

build:
	docker compose build

shell:
	docker compose exec api bash
