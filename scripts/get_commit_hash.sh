#!/usr/bin/env bash
# This script should be run from the root folder

# Get the latest commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)

# Write the commit hash to a file
printf "%s" "$COMMIT_HASH" > config/commit.toml