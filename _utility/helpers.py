# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import csv
import pandas as pd
from datetime import datetime


def get_curr_date_time(strft="%Y_%b_%d_%H.%M.%S"):
    return datetime.now().strftime(strft)


def get_output_file(client_name='', extra='', extension="csv"):
    if not extra == "":
        return f"{client_name}_{extra}_{get_curr_date_time()}.{extension}"
    else:
        return f"{client_name}_{get_curr_date_time()}.{extension}"


def csv_get_column(csv_file, column_name):
    tmp = []
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tmp.append(row[column_name])
    return tmp


def csv_add_column(csv_file, header_list, list_of_data, outfile):
    df = pd.read_csv(csv_file)
    for index, head in enumerate(header_list):
        df[head] = list_of_data[index]

    df.to_csv(outfile)
