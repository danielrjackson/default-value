CONFIG := .config
CACHE  := .cache

PY      := python -m

.PHONY: lint test docs clean

lint:
	ruff check . \
		--config $(CONFIG)/ruff.toml \
		--cache-dir $(CACHE)/ruff
	mypy src tests --config-file $(CONFIG)/mypy.ini

test:
	coverage run --rcfile $(CONFIG)/.coveragerc -m pytest
	coverage html --rcfile $(CONFIG)/.coveragerc

docs:
	mkdocs serve -f $(CONFIG)/mkdocs.yml

clean:
	rm -rf $(CACHE) .pytest_cache .coverage htmlcov dist
