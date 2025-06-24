.PHONY: alembic

alembic:
	alembic revision --autogenerate -m "migration run"
	alembic upgrade head
up:
	sudo docker compose up --build
lint:
	poetry run isort .
	poetry run black .
