#!/bin/bash -e

HOME="/home/developer"

if [ -e "$HIME/app.log" ] then
  mv "$HIME/app.log" "$HOME/app_`date --iso-8601=seconds`.log"
fi

APP_LOG="$HOME/app.log"
MOSQUITTO_LOG="$HOME/msqt.log"
WEB_HELPER_LOG="$HOME/web_helper.log"

nohup mosquitto -c "/etc/mosquitto/no_auth.conf" > "$MOSQUITTO_LOG" 2>&1 &

nohup python3 "$HOME/server-adm/mqtt/web_helper.py" > "$WEB_HELPER_LOG" 2>&1 &

nohup java -jar "$HOME/app.jar" > "$APP_LOG" 2>&1 &

exit 0