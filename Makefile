test-coverage:
	@python -Wmodule -m coverage run -m unittest

coverage-report:
	@coverage report -m --fail-under 100

test:
	@$(MAKE) --no-print-directory test-coverage
	@$(MAKE) --no-print-directory coverage-report
	@flake8 .
