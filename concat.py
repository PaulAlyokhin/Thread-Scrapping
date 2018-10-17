#!/usr/bin/env python3

import os
import pandas as pd
import xlsxwriter


def save(result, x):
    """
    This function saves the results(concatenated dataframes) into an Excel file.
    :param result: concatenated dataframes
    :param x: number of dataframes
    """
    filename = 'New %s files.xlsx' % x
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    result.to_excel(writer)
    writer.save()


files = []
path = '.'
filenames = os.listdir(path)
for filename in filenames:
    if filename.startswith('Output'):
        fil = pd.read_excel(filename)
        files.append(fil)

a = 0
for x in range(1, len(files) + 1):
    if x % 11 == 0:
        result = pd.concat(files[a:x], ignore_index=True)
        save(result, x)
        a += 11
    elif x == len(files):
        result = pd.concat(files[a:x], ignore_index=True)
        save(result, x)
