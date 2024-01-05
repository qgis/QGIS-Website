help:
		@echo "hugo-bulma-blocks-theme"
		@echo 
		@echo "Brought to you by Kartoza (Pty) Ltd."
		@echo 
		@echo "Help for using this Makefile"
		@echo
		@echo "For detailed help please visit:"
		@echo "https://github.com/kartoza/hugo-bulma-blocks-theme"
		@echo
		@echo "------------------------------------------------------------------"
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m - %s\n", $$1, $$2}'
 
dev-build: ## Generate the development docker container
	docker build --rm -f Dockerfile.dev -t kartoza_hugo_dev:latest .

dev: dev-build ## Run the development hugo container
	docker run --rm -it -v "$${PWD}":/app -w /app -p $${HOST_IP:-127.0.0.1}:1313:1313 kartoza_hugo_dev:latest

dev-metrics: dev-build ## Run the development hugo container with metrics
	docker run --rm -it -v "$${PWD}":/app -w /app -p $${HOST_IP:-127.0.0.1}:1313:1313 kartoza_hugo_dev:latest serve -D --bind 0.0.0.0 --templateMetrics --templateMetricsHints

deploy-prod: ## Deploy everything to production
	docker build -t bulma-blocks .
	docker-compose -f ~/docker-compose.yml up -d bulma_blocks_prod
	docker image prune -af

tests: ## Run the test suite
	docker build --rm -f Dockerfile.tests -t hugo_tests:latest .
	docker run --rm --net=host --volume "$${PWD}":/app -w /app hugo_tests:latest

build: ## Build the site then run using python http.server
	hugo
	python -m http.server 8000 -d public
	#xdg-open http://localhost:8000
