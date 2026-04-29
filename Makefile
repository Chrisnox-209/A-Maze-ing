MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports \
--disallow-untyped-defs --check-untyped-defs
MAIN = a_maze_ing.py
CONFIG = config.txt


.PHONY: run, install, clean, build, lint

install:
	@python3 -m poetry install

run:
	@python3 -m poetry run python3 $(MAIN) $(CONFIG)

clean:
	@find . -name "__pycache__" -o -name ".mypy_cache" -o -name "dist" | xargs rm -rf
	@rm -f *.whl *.tar.gz
	@echo "All code clean"

build:
	@echo "Building project.."
	@cd maze_core && python3 -m poetry  build
	@cd maze_core && mv dist/*  ../
	@rm -R maze_core/dist

debug:
	@python3 -m poetry run python3 -m pdb $(MAIN) $(CONFIG)


lint:
		poetry run python3 -m flake8 .\
		poetry run python3 -m mypy . $(MYPY_FLAGS)\