.PHONY: devel-install install format format-check devel-build devel-install test

install:
	@pip install -r requirements.txt

test:
	@pytest tests

start:
	@bash ./start.sh
