help:
	@echo "OSGeo Hugo Website"
	@echo
	@echo "Help for using this Makefile"
	@echo
	@echo "For detailed help please visit:"
	@echo "https://github.com/OSGeo/osgeo-hugo"
	@echo
	@echo "------------------------------------------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m - %s\n", $$1, $$2}'

# ----------------------------------------------------------------------------
#    P R O D U C T I O N     C O M M A N D S
# ----------------------------------------------------------------------------

build: ## Build the site for production
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building site in production"
	@echo "------------------------------------------------------------------"
	hugo --config config.toml,config/config.prod.toml

deploy: ## Deploy the site (pull, backup, rebuild)
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Deploy site in production"
	@echo "------------------------------------------------------------------"
	git pull && rm -rf archive; mkdir -p archive; [ -d public_prod ] && mv public_prod archive/ || true; make build

revert-deploy: ## Revert to previous deployment
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Revert to the previous state in production"
	@echo "------------------------------------------------------------------"
	rm -rf public_prod; [ -d archive/public_prod ] && cp -r archive/public_prod ./ || echo "No backup found"

# ----------------------------------------------------------------------------
#    D E V E L O P M E N T     C O M M A N D S
# ----------------------------------------------------------------------------

hugo-dev-build: ## Build the site locally and run a python server at localhost:8000
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building site in development"
	@echo "------------------------------------------------------------------"
	hugo --config config.toml,config/config.dev.toml
	python3 -m http.server 8000 -d public_dev

hugo-run-dev: ## Run the Hugo dev server at localhost:1313
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Starting Hugo development server"
	@echo "------------------------------------------------------------------"
	hugo server $(HUGOSERVERFLAGS) --config config.toml,config/config.dev.toml

hugo-run-drafts: ## Run Hugo dev server with drafts enabled
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Starting Hugo development server (with drafts)"
	@echo "------------------------------------------------------------------"
	hugo server --buildDrafts $(HUGOSERVERFLAGS) --config config.toml,config/config.dev.toml

# ----------------------------------------------------------------------------
#    F O R M A T T I N G     &     L I N T I N G
# ----------------------------------------------------------------------------

format: ## Format all Markdown and HTML files with Prettier
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Formatting files with Prettier"
	@echo "------------------------------------------------------------------"
	npx prettier --write "content/**/*.md" "themes/**/*.html" "themes/**/*.css" "themes/**/*.sass" "themes/**/*.scss"

format-check: ## Check formatting without making changes
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Checking formatting with Prettier"
	@echo "------------------------------------------------------------------"
	npx prettier --check "content/**/*.md" "themes/**/*.html"

lint: ## Run all linters
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running linters"
	@echo "------------------------------------------------------------------"
	@$(MAKE) lint-md || true
	@$(MAKE) lint-html || true
	@echo "Linting complete"

lint-md: ## Lint Markdown files
	@echo "Linting Markdown..."
	npx markdownlint-cli "content/**/*.md" || true

lint-html: ## Lint HTML output (requires build first)
	@echo "Linting HTML..."
	@[ -d public ] && npx htmlhint "public/**/*.html" || echo "Run 'make build' first"

# ----------------------------------------------------------------------------
#    P R E - C O M M I T
# ----------------------------------------------------------------------------

pre-commit: ## Run pre-commit hooks on all files
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running pre-commit hooks"
	@echo "------------------------------------------------------------------"
	pre-commit run --all-files

pre-commit-install: ## Install pre-commit hooks
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Installing pre-commit hooks"
	@echo "------------------------------------------------------------------"
	pre-commit install

# ----------------------------------------------------------------------------
#    U T I L I T Y     C O M M A N D S
# ----------------------------------------------------------------------------

clean: ## Clean all build artifacts
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Cleaning build artifacts"
	@echo "------------------------------------------------------------------"
	rm -rf public public_dev public_prod resources/_gen

open: ## Open the dev site in browser
	@echo "Opening http://localhost:1313"
	@xdg-open http://localhost:1313 2>/dev/null || open http://localhost:1313 2>/dev/null || echo "Could not open browser"

nix-shell: ## Enter the Nix development shell
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Entering Nix development shell"
	@echo "------------------------------------------------------------------"
	nix develop

new-page: ## Create a new content page (usage: make new-page PATH=about/contact)
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Creating new page"
	@echo "------------------------------------------------------------------"
ifdef PATH
	hugo new $(PATH)/_index.md
else
	@echo "Usage: make new-page PATH=section/name"
endif

new-post: ## Create a new news post (usage: make new-post TITLE="My Post")
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Creating new news post"
	@echo "------------------------------------------------------------------"
ifdef TITLE
	hugo new news/$(shell date +%Y-%m-%d)-$(shell echo "$(TITLE)" | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md
else
	@echo "Usage: make new-post TITLE=\"Post Title\""
endif

.PHONY: help build deploy revert-deploy hugo-dev-build hugo-run-dev hugo-run-drafts \
        format format-check lint lint-md lint-html pre-commit pre-commit-install \
        clean open nix-shell new-page new-post
