.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: venv
venv:
	python3 -m venv venv
	source venv/bin/activate 
	@echo "Activate with: source venv/bin/activate"

.PHONY: run
run:
	python3 main.py

.PHONY: clean
clean:
	rm -rf */**__pycache__
	rm -rf */**.mypy_cache

.PHONY: lint
lint:
	flake8 . && mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs