#!/bin/bash

# Variables
DB_NAME="postgres"
DB_USER="odoo"
DB_PASSWORD="G6QXbAZsAzUvMA5S7Kad66HhUSQLPGFP"
POSTGRES_SERVICE="db-odoo-supco"
BACKUP_DIR="./backup/"
DATE=$(date +%Y%m%d_%H%M%S)

# Backup
docker exec -t $POSTGRES_SERVICE pg_dump -U $DB_USER -d $DB_NAME -F c -b -v -f /tmp/db_backup_$DB_NAME_$DATE
docker cp $POSTGRES_SERVICE:/tmp/db_backup_$DB_NAME_$DATE $BACKUP_DIR/db_backup_$DB_NAME_$DATE
docker exec -t $POSTGRES_SERVICE rm /tmp/db_backup_$DB_NAME_$DATE

echo "Backup for database $DB_NAME completed!"