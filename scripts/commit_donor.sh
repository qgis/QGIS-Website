#!/usr/bin/env bash
#!encoding: UTF-8

# set scripts dir as cwd
#cd "${0%/*}"

if [ -f running ]; then
    echo "$0 still running"
    exit 1
fi
touch running

# git pull --rebase

./scripts/add_donor.py $1

# git commit -a -m "Donor $1 added"

# git push origin main

rm running
exit 0

