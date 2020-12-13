#!/bin/bash -e

HOME="/home/developer"
LOG="$HOME/app_`date --iso-8601=seconds`.log"

nohup java -jar "$HOME/app.jar" > "$LOG" 2>&1 &

exit 0
