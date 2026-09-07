{
  description = "OSGeo Website";

  # nixConfig = {
  #   extra-substituters = [ "https://example.cachix.org" ];
  #   extra-trusted-public-keys = [ "example.cachix.org-1:xxxx=" ];
  # };

  inputs = {
    nixpkgs-version.url = "github:QGIS/qgis-nixpkgs-version";
    # Stable channel supplies the bulk of the toolchain (python, make).
    nixpkgs.follows = "nixpkgs-version/nixpkgs-26-05";
    # Hugo moves fast and stable lags a few releases behind, so the site
    # generator itself is taken from unstable to track the current release.
    nixpkgs-unstable.follows = "nixpkgs-version/nixpkgs-unstable";
  };

  outputs =
    {
      self,
      nixpkgs,
      nixpkgs-unstable,
      ...
    }:

    let
      # Flake system
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      nixpkgsFor = forAllSystems (
        system:
        import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        }
      );
      # Only used to pull the latest Hugo; everything else comes from stable.
      unstableFor = forAllSystems (
        system:
        import nixpkgs-unstable {
          inherit system;
          config.allowUnfree = true;
        }
      );
      hugoFor = forAllSystems (system: unstableFor.${system}.hugo);

    in
    {
      #
      ### PACKAGES
      #

      packages = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
        in
        rec {
          website = pkgs.callPackage ./nix/package.nix { hugo = hugoFor.${system}; };
          default = website;
        }
      );

      #
      ### APPS
      #

      apps = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
          inherit (nixpkgs) lib;

          wwwLauncher = pkgs.writeShellApplication {
            name = "website";
            runtimeInputs = [ pkgs.python3 ];
            text = ''
              exec ${lib.getExe pkgs.python3} \
                -m http.server 8000 \
                -d ${self.packages.${system}.website}/public_www/
            '';
          };

          # Python env for the content verifier with all required libraries
          # provisioned from nixpkgs (no pip/npm).
          verifyPython = pkgs.python3.withPackages (ps: [
            ps.requests
            ps.beautifulsoup4
            ps.lxml
            ps.html2text
            ps.rich
          ]);

          verifyLauncher = pkgs.writeShellApplication {
            name = "verify-content";
            runtimeInputs = [ verifyPython pkgs.git ];
            text = ''
              # Locate the project root so the script works from any
              # subdirectory. Honour an explicit override first.
              if [[ -z "''${OSGEO_HUGO_ROOT:-}" ]]; then
                if root="$(git rev-parse --show-toplevel 2>/dev/null)"; then
                  export OSGEO_HUGO_ROOT="$root"
                else
                  export OSGEO_HUGO_ROOT="$PWD"
                fi
              fi
              exec ${verifyPython}/bin/python3 \
                "$OSGEO_HUGO_ROOT/scripts/verify_content.py" "$@"
            '';
          };
        in
        rec {
          website = {
            type = "app";
            program = "${wwwLauncher}/bin/website";
          };
          verify-content = {
            type = "app";
            program = "${verifyLauncher}/bin/verify-content";
          };
          default = website;
        }
      );

      #
      ### SHELLS
      #

      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
        in
        {
          # Development environment
          default = pkgs.mkShell {
            packages = [
              hugoFor.${system} # Hugo (latest release, from nixpkgs-unstable)
              # One interpreter carrying every library the scripts in
              # scripts/ import, so `python3 scripts/<name>.py` works
              # directly in the dev shell. Keep in step with
              # REQUIREMENTS.txt.
              #
              # NOTE: atoma (used by fetch_feeds.py) is not packaged in
              # nixpkgs, so that one script still needs the pipenv
              # environment until we add a derivation for it.
              (pkgs.python3.withPackages (ps: [
                ps.beautifulsoup4 # HTML parsing for harvesters
                ps.boto3 # S3 download listings
                ps.html2text # HTML to markdown conversion
                ps.icalendar # Release schedule .ics generation
                ps.lxml # Fast HTML/XML parser backend
                ps.pillow # Logo/image resizing
                ps.python-dateutil # Feed date parsing
                ps.requests # HTTP client
                ps.rich # Pretty terminal tables
                ps.stripe # Donation sync
                ps.pytest # Test runner
              ]))
            ]
            ++ (with pkgs; [
              gnumake # GNU Make for build automation
            ]);
            shellHook = ''
              export DIRENV_LOG_FORMAT=
              echo "-----------------------"
              echo "🌈 Your Hugo Dev Environment is ready."
              echo "It provides hugo and python for the OSGeo Website Project."
              echo ""
              echo "🪛 Editor:"
              echo "--------------------------------"
              echo "This project is set up for Neovim; see .nvim.lua for"
              echo "project-local configuration."
              echo ""
              echo "🪛 Hugo:"
              echo "--------------------------------"
              echo "Start Hugo like this:"
              echo ""
              echo "hugo server"
              echo "-----------------------"
            '';
          };
        }
      );
    };
}
