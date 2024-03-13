gsutil mv base.py gs://price_bucket134567

bq load --ignore_unknown_values caiso_price.t2 bas.csv schema2.json