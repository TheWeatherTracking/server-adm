#!/bin/bash -e

LOG="update_`date --iso-8601=seconds`.log"
echo '' > "$LOG"

DB_NAME="dev_db"

INIT_SQL=`cat ./init.sql`
CREATE_TABLES_SQL=`cat ./create_tables.sql`
FILL_TEST_DATA_SQL=`cat ./fill_test_data.sql`

echo "$INIT_SQL" | sudo su - postgres -c "psql" | tee -a "$LOG"

echo "$CREATE_TABLES_SQL" | sudo su - postgres -c "psql -d $DB_NAME" | tee -a "$LOG"

echo "$FILL_TEST_DATA_SQL" | sudo su - postgres -c "psql -d $DB_NAME" > /dev/null

echo "Inserted" | tee -a "$LOG"

exit 0
