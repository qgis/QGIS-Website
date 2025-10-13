#!/usr/bin/env bash

# ----------------------------------------------
# User-adjustable parameters
# ----------------------------------------------

VSCODE_PROFILE="QGISWebSite"
EXT_DIR=".vscode-extensions"
VSCODE_DIR=".vscode"
LOG_FILE="vscode.log"

REQUIRED_EXTENSIONS=(
naumovs.color-highlight@2.8.0
devonray.snippet@1.1.0
GitHub.copilot@1.250.0
CelianRiboulet.webvalidator@1.3.1
eliostruyf.vscode-hugo-themer@1.2.0
GitHub.vscode-pull-request-github@0.80.1
ms-python.debugpy@2025.8.0
ms-playwright.playwright@1.1.14
streetsidesoftware.code-spell-checker@3.0.1
GitHub.copilot-chat@0.12.2
syler.sass-indented@1.8.33
GitHub.copilot-chat@0.23.2
arthaud-proust.hugo-partials-defs@0.4.0
kaellarkin.hugo-shortcode-syntax@2.3.0
GitHub.copilot@1.234.0
ms-python.python@2025.6.1
teabyii.ayu@1.0.5
esbenp.prettier-vscode@11.0.0
akmittal.hugofy@0.1.1
eamodio.gitlens@17.1.1
zhuangtongfa.material-theme@3.19.0
HitkoDev.vscode-remark-hugo@0.2.13
kaellarkin.hugo-shortcode-syntax@2.4.0
ms-python.vscode-pylance@2025.4.1
)

# ----------------------------------------------
# Functions
# ----------------------------------------------

launch_vscode() {
    code --user-data-dir="$VSCODE_DIR" \
        --profile="${VSCODE_PROFILE}" \
        --extensions-dir="$EXT_DIR" "$@"
}

list_installed_extensions() {
    find "$EXT_DIR" -maxdepth 1 -mindepth 1 -type d | while read -r dir; do
        pkg="$dir/package.json"
        if [[ -f "$pkg" ]]; then
            name=$(jq -r '.name' <"$pkg")
            publisher=$(jq -r '.publisher' <"$pkg")
            version=$(jq -r '.version' <"$pkg")
            echo "${publisher}.${name}@${version}"
        fi
    done
}

clean() {
    rm -rf .vscode .vscode-extensions
}
print_help() {
    cat <<EOF
Usage: $(basename "$0") [OPTIONS]

This script sets up and launches VSCode with a custom profile and extensions for the GeoSight Documentation project.

Actions performed:
    - Checks for required files and directories
    - Ensures VSCode and Docker are installed
    - Initializes VSCode user and extension directories if needed
    - Updates VSCode settings for commit signing, formatters, and linters (Markdown, Shell, Python)
    - Installs all required VSCode extensions
    - Launches VSCode with the specified profile and directories

Options:
    --help             Show this help message and exit
    --verbose          Print final settings.json contents before launching VSCode
    --list-extensions  List installed VSCode extensions in the custom extensions directory
    --clean            Remove the .vscode and .vscode-extensions directories completely

EOF
}

# Parameter handler
for arg in "$@"; do
    case "$arg" in
        --help)
            print_help
            exit 0
            ;;
        --verbose)
            # Handled later in the script
            ;;
        --list-extensions)
            echo "Installed extensions:"
            list_installed_extensions
            exit 0
            ;;
        --clean)
            echo "Remove .vscode and .vscode-extensions folders:"
            clean
            exit 0
            ;;
        *) ;;
    esac
done

# ----------------------------------------------
# Script starts here
# ----------------------------------------------

# Create .env file for VSCode
ENV_FILE=".env"

echo "Creating VSCode .env file..."
cat <<EOF >"$ENV_FILE"
PYTHONPATH=.venv
EOF

echo "✅ .env file created successfully!"
echo "Contents of .env:"
cat "$ENV_FILE"

# Also set the python path in this shell in case we want to run tests etc from the command line
export PYTHONPATH=$PYTHONPATH:.venv

echo "🗨️ Checking VSCode is installed ..."
if ! command -v code &>/dev/null; then
    echo "  ❌ 'code' CLI not found. Please install VSCode and add 'code' to your PATH."
    exit 1
else
    echo "  ✅ VSCode found ok."
fi

# Ensure .vscode directory exists
echo "🗨️  Checking if VSCode has been run before..."
if [ ! -d .vscode ]; then
    echo "  🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻"
    echo "  ⭐️ It appears you have not run vscode in this project before."
    echo "     After it opens, please close vscode and then rerun this script"
    echo "     so that the extensions directory initialises properly."
    echo "  🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺"
    mkdir -p .vscode
    mkdir -p .vscode-extensions
    # Launch VSCode with the sandboxed environment
    launch_vscode .
    exit 1
else
    echo "  ✅ VSCode directory found from previous runs of vscode."
fi

echo "🗨️ Checking HUGO is installed ..."
if ! command -v hugo &>/dev/null; then
   echo "  ❌ 'hugo' CLI not found. Please install it and ensure you have permissions to use it."
   exit 1
else
   echo "  ✅ hugo found ok."
fi

echo "🗨️ Checking if VSCode has been run before..."
if [ ! -d "$VSCODE_DIR" ]; then
    echo "  ⭐️ First-time VSCode run detected. Opening VSCode to initialize..."
    mkdir -p "$VSCODE_DIR"
    mkdir -p "$EXT_DIR"
    launch_vscode .
    exit 1
else
    echo "  ✅ VSCode directory detected."
fi

SETTINGS_FILE="$VSCODE_DIR/settings.json"

echo "🗨️ Checking if settings.json exists..."
if [[ ! -f "$SETTINGS_FILE" ]]; then
    echo "{}" >"$SETTINGS_FILE"
    echo "  🔧 Created new settings.json"
else
    echo "  ✅ settings.json exists"
fi

echo "🗨️ Updating git commit signing setting..."
jq '.["git.enableCommitSigning"] = true' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
echo "  🔧 git.enableCommitSigning enabled"

echo "🗨️ Ensuring markdown formatter is set..."
if ! jq -e '."[markdown]".editor.defaultFormatter' "$SETTINGS_FILE" >/dev/null; then
    jq '."[markdown]" += {"editor.defaultFormatter": "DavidAnson.vscode-markdownlint"}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Markdown formatter set"
else
    echo "  ✅ Markdown formatter already configured"
fi

echo "🗨️ Ensuring shell script formatter and linter are set..."
if ! jq -e '."[shellscript]".editor.defaultFormatter' "$SETTINGS_FILE" >/dev/null; then
    jq '."[shellscript]" += {"editor.defaultFormatter": "foxundermoon.shell-format", "editor.formatOnSave": true}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Shell script formatter set to foxundermoon.shell-format, formatOnSave enabled"
else
    echo "  ✅ Shell script formatter already configured"
fi

if ! jq -e '.["shellcheck.enable"]' "$SETTINGS_FILE" >/dev/null; then
    jq '. + {"shellcheck.enable": true}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 ShellCheck linting enabled"
else
    echo "  ✅ ShellCheck linting already configured"
fi

if ! jq -e '.["shellformat.flag"]' "$SETTINGS_FILE" >/dev/null; then
    jq '. + {"shellformat.flag": "-i 4 -bn -ci"}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Shell format flags set (-i 4 -bn -ci)"
else
    echo "  ✅ Shell format flags already configured"
fi
echo "🗨️ Ensuring global format-on-save is enabled..."
if ! jq -e '.["editor.formatOnSave"]' "$SETTINGS_FILE" >/dev/null; then
    jq '. + {"editor.formatOnSave": true}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Global formatOnSave enabled"
else
    echo "  ✅ Global formatOnSave already configured"
fi

# Python formatter and linter
echo "🗨️ Ensuring Python formatter and linter are set..."
if ! jq -e '."[python]".editor.defaultFormatter' "$SETTINGS_FILE" >/dev/null; then
    jq '."[python]" += {"editor.defaultFormatter": "ms-python.black-formatter"}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Python formatter set to Black"
else
    echo "  ✅ Python formatter already configured"
fi

if ! jq -e '.["python.linting.enabled"]' "$SETTINGS_FILE" >/dev/null; then
    jq '. + {"python.linting.enabled": true, "python.linting.pylintEnabled": true}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Python linting enabled (pylint)"
else
    echo "  ✅ Python linting already configured"
fi

echo "🗨️ Ensuring Python Testing Env is set..."
if ! jq -e '."[python]".editor.pytestArgs' "$SETTINGS_FILE" >/dev/null; then
    jq '."[python]" += {"editor.pytestArgs": "test"}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Python test set up"
else
    echo "  ✅ Python tests already configured"
fi
if ! jq -e '."[python]".testing.unittestEnabled' "$SETTINGS_FILE" >/dev/null; then
    jq '. + {"python.editor.unittestEnabled": false, "python.testing.pytestEnabled": true}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Python unit test set up"
else
    echo "  ✅ Python unit tests already configured"
fi
echo "🗨️ Ensuring Python Env File is set..."
if ! jq -e '."[python]".envFile' "$SETTINGS_FILE" >/dev/null; then
    jq '."[python]" += {"envFile": "${workspaceFolder}/.env"}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Python Env file set up"
else
    echo "  ✅ Python Env File already configured"
fi

echo "🗨️ Ensuring SQL formatter is set..."
if ! jq -e '."[sql]".editor.defaultFormatter' "$SETTINGS_FILE" >/dev/null; then
    jq '."[sql]" += {"editor.defaultFormatter": "dorzey.vscode-sqlfluff", "editor.formatOnSave": true}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 SQL formatter set to dorzey.vscode-sqlfluff, formatOnSave enabled"
else
    echo "  ✅ SQL formatter already configured"
fi

echo "🗨️ Ensuring SQLFluff dialect is set to postgres..."
if ! jq -e '.["sqlfluff.dialect"]' "$SETTINGS_FILE" >/dev/null; then
    jq '. + {"sqlfluff.dialect": "postgres"}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 SQLFluff dialect set to postgres"
else
    echo "  ✅ SQLFluff dialect already configured"
fi

# Ensure Marp stylesheet is set for Marp themes
echo "🗨️ Ensuring Marp stylesheet is set for Marp themes..."
MARP_STYLE_PATH="presentations/slide-style.css"
if jq -e '.["markdown.marp.themes"]' "$SETTINGS_FILE" >/dev/null; then
    # Overwrite existing marp.themes
    jq --arg style "$MARP_STYLE_PATH" '.["markdown.marp.themes"] = [$style]' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Updated markdown.marp.themes to use $MARP_STYLE_PATH"
else
    # Add marp.themes
    jq --arg style "$MARP_STYLE_PATH" '. + {"markdown.marp.themes": [$style]}' "$SETTINGS_FILE" >"$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "  🔧 Added markdown.marp.themes with $MARP_STYLE_PATH"
fi

if [[ " $* " == *" --verbose "* ]]; then
    echo "🗨️ Final settings.json contents:"
    cat "$SETTINGS_FILE"
fi

# Add VSCode runner configuration

cat <<EOF >.vscode/launch.json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Hugo Live Fast",
            "type": "shell",
            // see tasks.json for definition
            "preLaunchTask": "dev local fastrender", // The name of the task defined above
            "request": "attach"
        },
        {
            "name": "Build Using Locally Installed Hugo",
            "type": "shell",
            // see tasks.json for definition
            "preLaunchTask": "build local", // The name of the task defined above
            "request": "attach"
        },
        {
            "name": "Hugo Live Debug",
            "type": "shell",
            // see tasks.json for definition
            "preLaunchTask": "dev local", // The name of the task defined above
            "request": "attach"
        },
        {
            "name": "Dev Build",
            "type": "shell",
            // see tasks.json for definition
            "preLaunchTask": "dev build", // The name of the task defined above
            "request": "attach"
        }
    ]
}
EOF

cat <<EOF >.vscode/tasks.json
{
    "version": "2.0.0",
    "command": "bash",
    "options": {
        "cwd": "${workspaceRoot}"
    },
    "args": ["-c"],
    "tasks": [
        {
            "label": "build local",
            "type": "shell",
            "command": "bash",
            "args": ["-c", "hugo"],
            "problemMatcher": [],
            "group": {
                "_id": "test",
                "isDefault": false
            }
        },
        {
            "label": "dev local fastrender",
            "type": "shell",
            "command": "bash",
            "args": ["-c", "hugo server"],
            "problemMatcher": [],
            "group": {
                "_id": "test",
                "isDefault": false
            }
        },
        {
            "label": "dev local",
            "type": "shell",
            "command": "bash",
            "args": [
                "-c",
                "hugo server -D --disableFastRender --debug --gc --ignoreCache --printPathWarnings --log --verbose --verboseLog"
            ],
            "problemMatcher": [],
            "group": {
                "_id": "test",
                "isDefault": false
            }
        }
    ]
}
EOF


echo "🗨️ Installing required extensions..."
for ext in "${REQUIRED_EXTENSIONS[@]}"; do
    if echo "$installed_exts" | grep -q "^${ext}$"; then
        echo "  ✅ Extension ${ext} already installed."
    else
        echo "  📦 Installing ${ext}..."
        # Capture both stdout and stderr to log file
        if launch_vscode --install-extension "${ext}" >>"$LOG_FILE" 2>&1; then
            # Refresh installed_exts after install
            installed_exts=$(list_installed_extensions)
            if echo "$installed_exts" | grep -q "^${ext}$"; then
                echo "  ✅ Successfully installed ${ext}."
            else
                echo "  ❌ Failed to install ${ext} (not found after install)."
                exit 1
            fi
        else
            echo "  ❌ Failed to install ${ext} (error during install). Check $LOG_FILE for details."
            exit 1
        fi
    fi
done

echo "🗨️ Launching VSCode..."
launch_vscode .
