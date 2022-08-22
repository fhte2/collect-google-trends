#!/usr/bin/env python
# coding: utf-8

import os
import sys
import argparse

from time import time

from pytrends.request import TrendReq
from pytrends import dailydata
import pandas as pd
import datetime as dt

from helper_functions import trim_month, check_date

from google.cloud import bigquery

def main(params):
    keyword = params.keyword
    start_date = params.start_date
    end_date = params.end_date
    project = params.project
    dataset = params.dataset

    start_year = int(start_date.split('-')[0])
    start_month = int(trim_month(start_date.split('-')[1]))
    end_year = int(end_date.split('-')[0])
    end_month = int(trim_month(end_date.split('-')[1]))
    table = keyword + '_' + start_date + '_' + end_date

    start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

    client = bigquery.Client(project=f'{project}')

    existing_table_ids = [tbl.table_id for tbl in client.list_tables(f'{dataset}')]

    if table in existing_table_ids:
        print(f'Table {dataset}.{table} already exists, not overwriting')
        sys.exit()

    is_date_valid = check_date(start_year, end_year, start_month, end_month)

    if is_date_valid: 
        
        print(start_year, start_month, end_year, end_month)

        df = dailydata.get_daily_data(keyword, start_year, start_month, end_year, end_month, geo = 'DE')

        df_filtered = df.loc[start_date:end_date, :]
        
        job = client.load_table_from_dataframe(df, f'{dataset}.{table}')

        print(
            f"Successfully loaded Google Trends data in the table {dataset}.{table}"
            )
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load Google trends data to BigQuery')

    parser.add_argument('--keyword', required=True, help='keyword you would like to extract the trend for')
    parser.add_argument('--start_date', required=True, help='start date for data, format YYYY-MM-DD')
    parser.add_argument('--end_date', required=True, help='end date for keyword, format YYYY-MM-DD')
    parser.add_argument('--project', required=True, help='GC project name')
    parser.add_argument('--dataset', required=True, help='dataset')

    args = parser.parse_args()

    main(args)