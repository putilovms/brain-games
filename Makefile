build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

install:
	poetry install

brain-games:
	poetry run brain-games


.PHONY: install brain-games build publish package-install
