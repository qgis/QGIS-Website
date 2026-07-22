{
  description = "QGIS Website";

  # nixConfig = {
  #   extra-substituters = [ "https://example.cachix.org" ];
  #   extra-trusted-public-keys = [ "example.cachix.org-1:xxxx=" ];
  # };

  inputs = {
    nixpkgs-version.url = "github:QGIS/qgis-nixpkgs-version";
    nixpkgs.follows = "nixpkgs-version/nixpkgs-26-05";

    # Fetch the Hugo theme submodule directly as a flake input
    qgis-website-theme = {
      url = "github:qgis/QGIS-Hugo-Website-Theme";
      flake = false; # it's not a flake, just a source tree
    };
  };

  outputs =
    { self, nixpkgs, qgis-website-theme,... }:

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
          website = pkgs.callPackage ./nix/package.nix {
            theme = qgis-website-theme; # <-- pass the theme source in
            # Commit hash from the flake's git metadata (clean tree only;
            # falls back to the dirty short rev, then "unknown" for tarballs).
            commitHash = self.shortRev or self.dirtyShortRev or "unknown";
           };
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
        in
        rec {
          website = {
            type = "app";
            program = "${wwwLauncher}/bin/website";
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
          venvDir = "./.venv";
          pythonPackages = pkgs.python3Packages;
        in
        {
          # Development environment
          default = pkgs.mkShell {
            packages = with pkgs; [
              hugo # Hugo for building the website
              vscode # VSCode for development
              # A Python interpreter including the 'venv' module is required to bootstrap
              # the environment.
              pythonPackages.python

              # This executes some shell code to initialize a venv in $venvDir before
              # dropping into the shell
              pythonPackages.venvShellHook
              pythonPackages.icalendar # Python packages
              pythonPackages.requests # Python packages
              pythonPackages.pillow # Python packages
              pythonPackages.lxml # Python packages
              gnumake # GNU Make for build automation
              transifex-cli
              libxml2 # Required by lxml
              libxslt
            ];

            shellHook = ''
              export DIRENV_LOG_FORMAT=
              git submodule update --init --recursive
              SOURCE_DATE_EPOCH=$(date +%s)

              if [ -d "${venvDir}" ]; then
                echo "Skipping venv creation, '${venvDir}' already exists"
              else
                echo "Creating new venv environment in path: '${venvDir}'"
                # Note that the module venv was only introduced in python 3, so for 2.7
                # this needs to be replaced with a call to virtualenv
                ${pythonPackages.python.interpreter} -m venv "${venvDir}"
              fi

              # Under some circumstances it might be necessary to add your virtual
              # environment to PYTHONPATH, which you can do here too;
              # PYTHONPATH=$PWD/${venvDir}/${pythonPackages.python.sitePackages}/:$PYTHONPATH

              source "${venvDir}/bin/activate"

              pip install -r REQUIREMENTS.txt
    
              echo "-----------------------"
              echo "🌈 Your Hugo Dev Environment is ready."
              echo "It provides hugo and vscode for use with the QGIS Website Project"
              echo ""
              echo "🪛 VSCode:"
              echo "--------------------------------"
              echo "Start vscode like this:"
              echo ""
              echo "./vscode.sh"
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

      #
      ### CHECKS
      #

      checks = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
        in
        import ./nix/tests.nix {
          inherit pkgs;
          website = self.packages.${system}.website;
          devShell = self.devShells.${system}.default;
          websiteApp = self.apps.${system}.website.program;
        }
      );
    };
}
