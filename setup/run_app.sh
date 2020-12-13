#!/bin/bash -e

HOME="/home/developer"
LOG="$HOME/app_`date --iso-8601=seconds`.log"

if not ls "$HOME/app.jar" then
  echo 'No app.jar was found'
  exit 1
fi

nohup java -jar "$HOME/app.jar" > "$LOG" 2>&1 &

exit 0
