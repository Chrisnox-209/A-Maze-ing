.PHONY: run, install, clean, lint

install:
	@poetry install

run:
	@python3 -m poetry run python3 a_maze_ing.py

clean:
	@rm -rf */__pycache__
	@rm -rf */.mypy_cache
	@rm -rf __pycache__
	@rm -rf .mypy_cache
	@echo "All code clean"

lint:
	python3 -m flake8 . && python3 -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs