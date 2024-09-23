#!/usr/bin/env bash
#!encoding: UTF-8

# Set the scripts directory as the current working directory
# cd "${0%/*}"

# Define log file
LOG_FILE="/tmp/stripehook.log"

# Log function to append messages to the log file
log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" >> "$LOG_FILE"
}

# Check if the script is already running
if [ -f running ]; then
    log "$0 still running"
    exit 1
fi
touch running

# Log and execute git pull
log "Executing git pull"
git pull  --rebase >> "$LOG_FILE" 2>&1

# Log and execute add_donor.py script
log "Adding donor: $1"
./scripts/add_donor.py "$1" >> "$LOG_FILE" 2>&1

# Log and execute git commit
log "Committing donor $1"
git commit -a -m "Donor $1 added" >> "$LOG_FILE" 2>&1

# Log and execute git push
log "Pushing changes to origin main"
git push origin main >> "$LOG_FILE" 2>&1

# Cleanup
rm running
log "Script completed successfully"
exit 0