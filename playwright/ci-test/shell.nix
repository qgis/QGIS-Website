#
# Development shell for the Playwright end-to-end tests.
#
# The nixpkgs revision below is deliberately kept in step with the
# `nixpkgs-unstable` input locked in the repository root `flake.lock`, so the
# browsers used locally match the toolchain the rest of the project is built
# with. When you bump `flake.lock`, bump this revision to match.
#
# This revision provides playwright-test/playwright-driver 1.61.1, which is why
# package.json pins @playwright/test and playwright to exactly 1.61.1 (no
# caret): the client and the browser bundle must be the same revision, both
# here and in CI. Bump both together.
#
let
  nixpkgs = builtins.fetchTarball "https://github.com/NixOS/nixpkgs/archive/83199d0d373dd3ac2b9a1996b1d0263f76ab7a4c.tar.gz";
  pkgs = import nixpkgs { config = { }; overlays = [ ]; };
in
with pkgs;
mkShell {
  buildInputs = [
    nodejs
    playwright-test
    python3Packages.playwright
    python3Packages.pytest
  ];

  PLAYWRIGHT_BROWSERS_PATH = "${pkgs.playwright-driver.browsers}";

  shellHook = ''
    # Remove playwright from node_modules, so it will be taken from playwright-test
    rm -rf node_modules/@playwright
    export PLAYWRIGHT_BROWSERS_PATH=${pkgs.playwright-driver.browsers}
    export PLAYWRIGHT_SKIP_VALIDATE_HOST_REQUIREMENTS=true
  '';
}
