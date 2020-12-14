#!/bin/bash -e

HOME="/home/developer"

if [ -e "$HOME/app.log" ]; then
  mv "$HOME/app.log" "$HOME/app_`date --iso-8601=seconds`.log"
fi

APP_LOG="$HOME/app.log"
MOSQUITTO_LOG="$HOME/msqt.log"
WEB_HELPER_LOG="$HOME/web_helper.log"

echo 'port 1883\nallow_anonymous true' > "/etc/mosquitto/no_auth.conf"

nohup "/usr/sbin/mosquitto" -c "/etc/mosquitto/no_auth.conf" > "$MOSQUITTO_LOG" 2>&1 &

nohup python3 "$HOME/server-adm/mqtt/web_helper.py" > "$WEB_HELPER_LOG" 2>&1 &

nohup java -jar "$HOME/app.jar" > "$APP_LOG" 2>&1 &

chown -R developer /home/developer 
chgrp -R developer /home/developer 

exit 0

