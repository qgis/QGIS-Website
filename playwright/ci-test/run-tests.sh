#!/usr/bin/env bash

source playwright-path.sh

echo "This script will run the tests defined in tests/"
echo ""

$PLAYWRIGHT \
    test \
    --ui \
    --project chromium

echo "--done--"
