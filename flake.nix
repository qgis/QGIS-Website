{
  description = "QGIS Website";

  # nixConfig = {
  #   extra-substituters = [ "https://example.cachix.org" ];
  #   extra-trusted-public-keys = [ "example.cachix.org-1:xxxx=" ];
  # };

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:

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
          website = pkgs.callPackage ./nix/package.nix { };
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
        in
        {
          # Development environment
          default = pkgs.mkShell {
            packages = with pkgs; [
              hugo # Hugo for building the website
              vscode # VSCode for development
              python3Packages.icalendar # Python packages
              python3Packages.requests # Python packages
              gnumake # GNU Make for build automation
            ];
            shellHook = ''
              export DIRENV_LOG_FORMAT=
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
