This frameworks pulls data from the California electric grid. This example pulls the Hour-Ahead prices hourly and compares it against the Day Ahead Price.

1. base.py queries CAISO OASIS using variables.py
2. base.py then extracts and reformats to insertion into BigQuery
3. move.sh is a GCP script that moves the extracted CSV from CAISO into the DB
4. cron.tab.txt is a copy of the crontab on the Compute Engine.

5. https://lookerstudio.google.com/reporting/3004e21a-2ad6-4992-b9b4-18176e754b7f
