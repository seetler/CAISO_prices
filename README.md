This frameworks pulls data from the California electric grid CAISO using their Open Access Information System (OASIS) on a Google Cloud stack. This example pulls the Hour-Ahead prices hourly and compares it against the Day-Ahead Prices.

1. base.py queries CAISO OASIS using variables.py then extracts and reformats for insertion into BigQuery.
3. move.sh is a GCP script that moves the extracted CSV from CAISO into the DB.
4. cron.tab.txt is a copy of the crontab text on the Compute Engine.
6. staging_query.sql is a SQL view that formats the raw data for visualization.
5. https://lookerstudio.google.com/s/vU9CxzzAQbM
