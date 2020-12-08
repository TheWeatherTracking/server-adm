#!/bin/bash -e

LOG="update_`date --iso-8601=seconds`.log"
echo '' > "$LOG"

DB_NAME="dev_db"

INIT_SQL=`cat ./init.sql`
CREATE_TABLES_SQL=`cat ./create_tables.sql`



echo "$INIT_SQL" | sudo su - postgres -c "psql" | tee -a "$LOG"

echo "$CREATE_TABLES_SQL" | sudo su - postgres -c "psql -d $DB_NAME" | tee -a "$LOG"

exit 0
