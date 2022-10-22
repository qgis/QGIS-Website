dev-build:
	docker build --rm -f Dockerfile.dev -t qgis_hugo_dev:latest .

dev: dev-build
	docker run --rm -it -v "$${PWD}":/app -w /app -p $${HOST_IP:-127.0.0.1}:1313:1313 qgis_hugo_dev:latest

dev-build-metrics: dev-build
	docker run --rm -it -v "$${PWD}":/app -w /app -p $${HOST_IP:-127.0.0.1}:1313:1313 qgis_hugo_dev:latest serve -D --bind 0.0.0.0 --templateMetrics --templateMetricsHints

deploy-prod:
	docker build -t qgis.org .
	docker-compose -f ~/docker-compose.yml up -d qgis_hugo_prod
	docker image prune -af

tests:
	docker build --rm -f Dockerfile.tests -t qgis_hugo_tests:latest .
	docker run --rm --net=host --volume "$${PWD}":/app -w /app qgis_hugo_tests:latest
