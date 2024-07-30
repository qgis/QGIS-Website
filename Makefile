help:
	@echo "QGIS Website"
	@echo
	@echo "Brought to you by Kartoza (Pty) Ltd."
	@echo
	@echo "Help for using this Makefile"
	@echo
	@echo "For detailed help please visit:"
	@echo "https://github.com/QGIS/QGIS-Website"
	@echo
	@echo "------------------------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m - %s\n", $$1, $$2}'

# ----------------------------------------------------------------------------
#    D O C K E R     C O M M A N D S
# ----------------------------------------------------------------------------
 
dev-build: ## Generate the development docker container
	docker build --rm -f Dockerfile.dev -t qgis_hugo_dev:latest .

dev: dev-build ## Run the development hugo container
	docker run --rm -it -v "$${PWD}":/app -w /app -p $${HOST_IP:-127.0.0.1}:1313:1313 qgis_hugo_dev:latest

dev-metrics: dev-build ## Run the development hugo container with metrics
	docker run --rm -it -v "$${PWD}":/app -w /app -p $${HOST_IP:-127.0.0.1}:1313:1313 qgis_hugo_dev:latest serve -D --bind 0.0.0.0 --templateMetrics --templateMetricsHints

deploy-prod: ## Deploy everything to production
	docker build -t qgis.org .
	docker-compose -f ~/docker-compose.yml up -d qgis_hugo_prod
	docker image prune -af

tests: ## Run the test suite
	docker build --rm -f Dockerfile.tests -t qgis_hugo_tests:latest .
	docker run --rm --net=host --volume "$${PWD}":/app -w /app qgis_hugo_tests:latest


# ----------------------------------------------------------------------------
#    P R O D U C T I O N     C O M M A N D S
# ----------------------------------------------------------------------------

build: ## Build the site for nocache.qgis.org, www.qgis.org and qgis.org
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building site in production"
	@echo "------------------------------------------------------------------"
	hugo --config config.toml,config/config.nocache.toml
	hugo --config config.toml,config/config.prod.toml
	hugo --config config.toml,config/config.www.toml


deploy: ## Deploy the site for nocache.qgis.org, www.qgis.org and qgis.org
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Deploy site in production"
	@echo "------------------------------------------------------------------"
	git pull && rm -rf archive; mkdir archive; mv public_www public_prod public_nocache archive; make build

revert-deploy: ## Revert the site for nocache.qgis.org, www.qgis.org and qgis.org
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Revert to the previous state in production"
	@echo "------------------------------------------------------------------"
	rm -rf public_www public_prod public_nocache; cp -r archive/public_www archive/public_prod archive/public_nocache ./

# ----------------------------------------------------------------------------
#    D E V E L O P M E N T     C O M M A N D S
# ----------------------------------------------------------------------------

hugo-dev-build: ## Build the site localy and run a python server at localhost:8000 with hugo
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building site in development"
	@echo "------------------------------------------------------------------"
	hugo --config config.toml,config/config.dev.toml
	python3 -m http.server 8000 -d public_dev


hugo-run-dev: ## Run the server at localhost:1313 with hugo
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building site in development"
	@echo "------------------------------------------------------------------"
	hugo server --config config.toml,config/config.dev.toml


# ----------------------------------------------------------------------------
#    U T I L S     C O M M A N D S
# ----------------------------------------------------------------------------

csv/schedule.csv scripts/schedule.ics data/conf.json:
	python scripts/update-schedule.py

clearschedule:
	$(RM) csv/schedule.csv data/conf.json

schedule: clearschedule csv/schedule.csv scripts/schedule.ics data/conf.json	## Update schedule after release
	git pull --autostash --rebase
	git commit -a -m "Update for $(shell jq -r '.release' data/conf.json)/$(shell jq -r '.ltrrelease' data/conf.json) point releases"

.PHONY: schedule
