SHELL = /usr/bin/env bash -o pipefail
include .env

default: help

.PHONY: help
help:
	# Usage:
	@sed -n '/^\([a-z][^:]*\).*/s//    make \1/p' $(MAKEFILE_LIST)

.PHONY: clean
clean:
	rm -rf env \
	rm -rf .docker-data;


.PHONY: install
install:
	set -a; \
	source .env; \
	python3 -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt; \

.PHONY: test
test:
	set -a; \
	source .env; \
	source env/bin/activate; \
	pytest; \

.PHONY: databases/initdb
databases/initdb:
	set -a; \
	source .env; \
	source env/bin/activate; \
	python -m databases.create_tables; \

.PHONY: scheduler/collect
scheduler/collect:
	set -a; \
	source .env; \
	source env/bin/activate; \
	python -m components.scheduler_support.news_data_updater; \

.PHONY: data_collector/run
data_collector/run:
	set -a; \
	source .env; \
	source env/bin/activate; \
	gunicorn applications.data_collector.app:app --bind ${HOST}:${DATA_COLLECTOR_PORT}; \

.PHONY: data_analyzer/run
data_analyzer/run:
	set -a; \
	source .env; \
	source env/bin/activate; \
	gunicorn applications.data_analyzer.app:app --bind ${HOST}:${DATA_ANALYZER_PORT}; \

.PHONY: web_application/run
web_application/run:
	set -a; \
	source .env; \
	source env/bin/activate; \
	gunicorn applications.web_application.app:app --bind ${HOST}:${WEB_APPLICATION_PORT}; \
