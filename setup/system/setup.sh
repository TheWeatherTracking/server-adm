#!/bin/bash -e

LOGDIR="/var/log/custom/setup"
LOGFILE="$LOGDIR/setup_log.log"

cp "$LOGFILE" "$LOGDIR/`date --iso-8601=seconds`.log"
echo "Started at `date --iso-8601=seconds`" > "$LOGFILE"

adduser developer
# < insert pass twice
usermod -aG sudo developer
echo "Add user 'developer' into group sudo" >> "$LOGFILE"


yes | apt-get update | tee -a "$LOGFILE"

yes | apt-get install default-jre | tee -a "$LOGFILE"

yes | apt-get install git-all | tee -a "$LOGFILE"

sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt-get update

yes | apt-get install postgresql-10 | tee -a "$LOGFILE"

cd /home/developer/ && git clone "https://github.com/TheWeatherTracking/server-adm.git" | tee -a "$LOGFILE"

echo "Well done!" >> "$LOGFILE"

exit 0

