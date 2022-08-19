#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time

from google.cloud import bigquery

# import pandas as pd

def main(params):
    keyword = params.keyword
    start_date = params.start_date
    end_date = params.end_date
    project = params.project
    dataset = params.dataset
    table_name = params.table_name

    client = bigquery.Client()

    table_id = f"de-course-359719.google_trends.{table_name}"

    schema = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
]
    table = bigquery.Table(table_id, schema=schema)
        
    table = client.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )

    print("Testing function")
    print(keyword, start_date, end_date, table_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--keyword', required=True, help='keyword you would like to extract the trend for')
    parser.add_argument('--start_date', required=True, help='start date for data')
    parser.add_argument('--end_date', required=True, help='end date for keyword')
    parser.add_argument('--project', required=True, help='GC project name')
    parser.add_argument('--dataset', required=True, help='dataset')
    parser.add_argument('--table_name', required=True, help='table name')

    args = parser.parse_args()

    main(args)