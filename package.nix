{ lib, stdenv, hugo, gnumake }:

stdenv.mkDerivation {
    name = "qgis-website";
    src = lib.cleanSourceWith {
        src = ./.;
        filter = (
        path: type: (builtins.all (x: x != baseNameOf path) [
            ".git"
            ".github"
            "flake.nix"
            "package.nix"
        ])
        );
    };
    buildInputs = [ hugo gnumake ];

    buildPhase = ''
        make deploy
    '';

    installPhase = ''
        mkdir -p $out
        cp -r public_www public_prod $out/
    '';

    meta = with lib; {
        description = "A built QGIS website";
        license = licenses.mit;
    };
}

