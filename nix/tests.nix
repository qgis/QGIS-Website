{ pkgs, website, devShell, websiteApp }:

{
  # Verify build output structure
  test-build-output = pkgs.runCommand "test-build-output"
    {
      inherit website;
    }
    ''
      echo "Verifying build output structure..."
      
      if [ ! -d "${website}/public_www" ]; then
        echo "❌ public_www directory not found"
        exit 1
      fi
      
      echo "✅ public_www directory found"
      
      # Check for essential files
      if [ ! -f "${website}/public_www/index.html" ]; then
        echo "❌ index.html not found"
        exit 1
      fi
      
      echo "✅ index.html exists"
      
      # Verify directory is not empty
      file_count=$(find "${website}/public_www" -type f | wc -l)
      if [ "$file_count" -lt 10 ]; then
        echo "❌ Too few files in public_www (found: $file_count)"
        exit 1
      fi
      
      echo "✅ Build output contains $file_count files"
      echo "Build output verification passed" > $out
    '';

  # Test dev shell has required tools
  test-dev-shell = pkgs.runCommand "test-dev-shell"
    {
      nativeBuildInputs = devShell.nativeBuildInputs or [ ]
        ++ devShell.buildInputs or [ ];
    }
    ''
      echo "Testing dev shell tools..."
      
      # Check hugo is available
      if ! command -v hugo &> /dev/null; then
        echo "❌ hugo not found in dev shell"
        exit 1
      fi
      
      echo "✅ hugo available: $(hugo version)"
      
      # Check python is available
      if ! command -v python3 &> /dev/null; then
        echo "❌ python3 not found in dev shell"
        exit 1
      fi
      
      echo "✅ python3 available: $(python3 --version)"
      
      # Check make is available
      if ! command -v make &> /dev/null; then
        echo "❌ make not found in dev shell"
        exit 1
      fi
      
      echo "✅ make available: $(make --version | head -1)"
      
      echo "Dev shell verification passed" > $out
    '';

  # Test website app can be run
  test-website-app = pkgs.runCommand "test-website-app"
    {
      app = websiteApp;
      inherit website;
    }
    ''
      echo "Testing website app..."
      
      # Verify the app script exists and is executable
      if [ ! -x "$app" ]; then
        echo "❌ Website app not executable: $app"
        exit 1
      fi
      
      echo "✅ Website app is executable"
      
      # Verify it references the correct website path
      if ! grep -q "${website}/public_www" "$app"; then
        echo "❌ Website app doesn't reference correct path"
        exit 1
      fi
      
      echo "✅ Website app references correct public_www path"
      
      echo "Website app verification passed" > $out
    '';

  # Package builds successfully (implicit check)
  build-website = website;
}
