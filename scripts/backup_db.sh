#!/bin/bash
# backup_db.sh
# Utility script to backup all databases used in the project.
# This script can be scheduled via cron or run manually as part of CI.
#
# Usage:
#   ./backup_db.sh
#
# Example: Uses pg_dump for PostgreSQL databases.
# Ensure that environment variables (DB_HOST, DB_USER, DB_NAME, DB_PASSWORD) are set.
#
# Note: Adjust the command if using a different database system.

set -e

# Check if required environment variables are set
: "${DB_HOST:?Need to set DB_HOST}"
: "${DB_USER:?Need to set DB_USER}"
: "${DB_NAME:?Need to set DB_NAME}"
: "${DB_PASSWORD:?Need to set DB_PASSWORD}"

# Export DB password for pg_dump
export PGPASSWORD=$DB_PASSWORD

# Define backup file name with timestamp
BACKUP_FILE="backup_${DB_NAME}_$(date +'%Y%m%d_%H%M%S').sql"

echo "Starting backup for database '$DB_NAME' at host '$DB_HOST'..."
pg_dump -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -F c -b -v -f "$BACKUP_FILE"

echo "Backup completed successfully. Backup file: $BACKUP_FILE"

# Unset the PGPASSWORD variable for security
unset PGPASSWORD
