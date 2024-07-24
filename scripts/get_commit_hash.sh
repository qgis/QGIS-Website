#!/usr/bin/env bash

# Get the latest commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)

# Write the commit hash to a file
echo $COMMIT_HASH > ../config/commit.toml