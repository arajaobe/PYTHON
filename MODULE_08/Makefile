.PHONY: install run check shell clean

check:
	@command -v poetry >/dev/null 2>&1 || { echo "Poetry not found. Install with: pipx install poetry"; exit 1; }

install: check
	poetry install

run: install
	poetry run python code.py

shell:
	poetry shell

# Clean up lock file and venv
clean:
	rm -f poetry.lock
	poetry env remove --all
