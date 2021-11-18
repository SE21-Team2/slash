"""
This module generates a CSV file for the results of the search
"""
import csv
from datetime import datetime
import os


def write_csv(arr, product, file_path):
    """ Returns the CSV file with the naming nomenclature as 'ProductDate_Time'
        Parameters- product: product entered by the user,
                    file_path: path where the csv needs to be stored
        Returns- file_name: CSV file """
    os.chdir(file_path)
    keys = arr[0].keys()
    now = datetime.now()
    file_name = product + now.strftime("%m%d%y_%H%M") + '.csv'
    try:
        with open(file_name, "w", newline='', encoding='utf-8') as a_file:
            dict_writer = csv.DictWriter(a_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(arr)
            a_file.close()
    except OSError:
        # file not found
        print(f"File: ${file_name} not found")
    return file_name
