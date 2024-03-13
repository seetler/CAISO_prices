1. base.py queries CAISO OASIS using variable.py
2. base.py then extracts and reformats to insertion into BigQuery
3. move.sh is a GCP script that moves the extracted CSV from CAISO into the DB
4. cron.tab.txt is a copy of the crontab on the Compute Engine.
