{
  lib,
  stdenv,
  hugo,
  python3,
  theme, # the Hugo theme passed in from the flake
  commitHash,
}:

stdenv.mkDerivation {
  name = "qgis-website";

  src = lib.cleanSourceWith {
    src = ../.;
    filter = (
      path: type:
      (builtins.all (x: x != baseNameOf path) [
        ".git"
        ".github"
        "flake.nix"
        "flake.lock"
        "package.nix"
        "result"
      ])
    );
  };

  buildInputs = [
    hugo
    python3
  ];

  buildPhase = ''
    mkdir -p themes
    rm -rf themes/qgis-website-theme
    ln -s ${theme} themes/qgis-website-theme
    printf "%s" "${commitHash}" > config/commit.toml

    # Build qgis.org, then dedupe identical cross-language files into
    # relative symlinks to the base language (matches the Makefile build).
    hugo --config config.toml,config/config.prod.toml
    python3 scripts/dedup_public.py \
      --public-dir public_prod \
      --config config.toml \
      --base-lang en \
      --mode symlink

    # Build www.qgis.org and dedupe the same way.
    hugo --config config.toml,config/config.www.toml
    python3 scripts/dedup_public.py \
      --public-dir public_www \
      --config config.toml \
      --base-lang en \
      --mode symlink
  '';

  # -a preserves the dedup symlinks (plain cp -r would dereference them).
  installPhase = ''
    mkdir -p $out
    cp -a public_www public_prod $out/
  '';
  meta = with lib; {
    description = "A QGIS website";
    license = licenses.mit;
  };
}
