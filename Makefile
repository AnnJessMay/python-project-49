xinstall:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 hexlet_python_package

brain-even:
	poetry run python -m brain_games.scripts.brain_even

