# Ensure that this file has the correct permissions so that the container can access it
# You can run 'chmod +x ./mysql-init.sh' to grant the permissions
#!/bin/bash

DB_HOST="localhost"
DB_PORT="3306"
DB_NAME="dagster_data"
DB_USER="dagster_user"
DB_PASSWORD="dagster_password"

mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p"$DB_PASSWORD" -D "$DB_NAME" -e "CREATE TABLE POKEMON (
    name VARCHAR(100) PRIMARY KEY,
    type VARCHAR(50),
    hp INT,
    attack INT,
    defense INT
);"