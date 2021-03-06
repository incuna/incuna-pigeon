release:
	python setup.py register sdist bdist_wheel upload

test-coverage:
	@python -Wmodule -m coverage run -m unittest

coverage-report:
	@coverage report --fail-under 100

doctest:
	@python -m doctest README.md

test:
	@$(MAKE) --no-print-directory test-coverage
	@$(MAKE) --no-print-directory coverage-report
	@flake8 .
	@$(MAKE) --no-print-directory doctest
