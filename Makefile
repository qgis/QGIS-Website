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
#    P R O D U C T I O N     C O M M A N D S
# ----------------------------------------------------------------------------

build: ## Build the site for www.qgis.org and qgis.org
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building site in production"
	@echo "------------------------------------------------------------------"
	sh ./scripts/get_commit_hash.sh
	PUBLIC_DIR=public_prod CONFIG_PROD=config/config.prod.toml bash scripts/build_prod_per_lang.sh
	PUBLIC_DIR=public_www CONFIG_PROD=config/config.www.toml bash scripts/build_prod_per_lang.sh


deploy: ## Deploy the site for www.qgis.org and qgis.org
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Deploy site in production"
	@echo "------------------------------------------------------------------"
	git pull && rm -rf archive; mkdir archive; mv public_www public_prod archive; make build

revert-deploy: ## Revert the site for www.qgis.org and qgis.org
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Revert to the previous state in production"
	@echo "------------------------------------------------------------------"
	rm -rf public_www public_prod; cp -r archive/public_www archive/public_prod ./

# ----------------------------------------------------------------------------
#    D E V E L O P M E N T     C O M M A N D S
# ----------------------------------------------------------------------------

hugo-dev-build: ## Build the site locally and run a python server at localhost:8000 with hugo
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
	hugo server $(HUGOSERVERFLAGS) --config config.toml,config/config.dev.toml


# ----------------------------------------------------------------------------
#    U T I L S     C O M M A N D S
# ----------------------------------------------------------------------------

assets/csv/schedule.csv scripts/schedule.ics data/conf.json:
	python scripts/update-schedule.py

clearschedule:
	$(RM) assets/csv/schedule.csv data/conf.json

schedule: clearschedule assets/csv/schedule.csv scripts/schedule.ics data/conf.json	## Update schedule after release
	git pull --autostash --rebase
	git commit -a -m "Update for $(shell jq -r '.release' data/conf.json)/$(shell jq -r '.ltrrelease' data/conf.json) point releases"

.PHONY: schedule txpush txpull mktxtemp venv messages-extract messages-compile messages-generate tx-coverage tx-coverage-commit

TEMP:=tx-temp

venv:
	if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
	fi

mktxtemp:
	mkdir -p $(TEMP)

txpush: mktxtemp
	rm -rf $(TEMP)
	python3 scripts/tx_convert_push.py i18n/en.yml $(TEMP)/en.yml --lang en
	tx push -s

txpull: mktxtemp
	tx pull -a -f
	python3 scripts/tx_convert_pull.py $(TEMP) i18n

messages-extract:
	hugo-gettext extract translations/en/

messages-compile: fix-newlines
	hugo-gettext compile translations/

fix-newlines:
	@echo "Fixing newlines in translation files..."
	@python3 scripts/fix_newlines.py

generate-translations:
	hugo-gettext generate

clean-translations:
	@echo "Cleaning translated content..."
	@rm -rf content-translated/

# ----------------------------------------------------------------------------
#    T R A N S I F E X    C O V E R A G E
# ----------------------------------------------------------------------------

txcoverage: ## Fetch translation coverage from Transifex into data/tx_coverage.json (uses TX_TOKEN)
	@echo "Fetching translation coverage from Transifex..."
	python3 scripts/tx_fetch_coverage.py \
		--project qgis-website \
		--resources qgis-hugo-docs-md \
		--output data/tx_coverage.json

tx-coverage-commit: tx-coverage ## Fetch coverage and commit changes if file updated
	@echo "Committing updated coverage if changed..."
	@if [ -n "$(shell git status --porcelain data/tx_coverage.json)" ]; then \
		git config --global user.name 'GitHub Actions'; \
		git config --global user.email 'github-actions@github.com'; \
		git add data/tx_coverage.json; \
		git commit -m "Update translation coverage [skip ci]"; \
		echo "Committed coverage update."; \
	else \
		echo "No coverage changes."; \
	fi

