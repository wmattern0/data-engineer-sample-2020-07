import csv
import pathlib
import src.some_storage_library

"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""

def process_header():
    pass

def process_data():
    data_file = open(pathlib.Path('data/source/SOURCEDATA.txt'))
    data_reader = csv.reader(data_file)
    data_eng_sample_data = list(data_reader)
    print(data_eng_sample_data)

def write_data_engineer_sample():
    pass

if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    process_header()
    process_data()
    write_data_engineer_sample()
    print('Done the ETL process...')
