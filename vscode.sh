#!/usr/bin/env bash
echo "🪛 Installing VSCode Extensions:"
echo "--------------------------------"


# Ensure .vscode directory exists
mkdir -p .vscode
mkdir -p .vscode-extensions
# Define the settings.json file path
SETTINGS_FILE=".vscode/settings.json"

# Ensure settings.json exists
if [[ ! -f "$SETTINGS_FILE" ]]; then
    echo "{}" > "$SETTINGS_FILE"
fi

# Update settings.json non-destructively
echo "Updating VSCode settings.json..."
jq '.["git.enableCommitSigning"] = true' \
   "$SETTINGS_FILE" > "$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"

echo "✅ VSCode settings.json updated successfully!"
echo "Contents of settings.json:"
cat "$SETTINGS_FILE"

# Install required extensions
code --user-data-dir='.vscode' \
--profile='nix-config' \
--extensions-dir='.vscode-extensions' . \
--install-extension zhuangtongfa.material-theme@3.19.0 \
--install-extension naumovs.color-highlight@2.8.0 \
--install-extension GitHub.copilot@1.250.0 \
--install-extension teabyii.ayu@1.0.5 \
--install-extension ms-python.debugpy@2025.8.0 \
--install-extension ms-python.vscode-pylance@2025.5.1 \
--install-extension ms-python.python@2025.6.1 \
--install-extension syler.sass-indented@1.8.33 \
--install-extension GitHub.copilot-chat@0.26.7 \
--install-extension eamodio.gitlens@17.1.1 \
--install-extension devonray.snippet@1.1.0 \
--install-extension eliostruyf.vscode-hugo-themer@1.2.0 \
--install-extension arthaud-proust.hugo-partials-defs@0.4.0 \
--install-extension akmittal.hugofy@0.1.1 \
--install-extension kaellarkin.hugo-shortcode-syntax@2.4.0 \
--install-extension HitkoDev.vscode-remark-hugo@0.2.13 \
--install-extension ms-playwright.playwright@1.1.14 \

# Launch VSCode with the sandboxed environment
code --user-data-dir='.vscode' \
--profile='nix-config' \
--extensions-dir='.vscode-extensions' .
