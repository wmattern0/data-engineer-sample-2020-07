import csv
import pathlib
import src.some_storage_library

"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""

class DataEngineerSample:

    def process_header(self):
        header_file = open(pathlib.Path('data/source/SOURCECOLUMNS.txt'))
        header_reader = csv.reader(header_file, delimiter='|')
        data_eng_sample_headers = list(header_reader)
        print(data_eng_sample_headers)

    def process_data(self):
        data_file = open(pathlib.Path('data/source/SOURCEDATA.txt'))
        data_reader = csv.reader(data_file, delimiter='|')
        data_eng_sample_data = list(data_reader)
        print(data_eng_sample_data)

    def write_data_engineer_sample(self):
        pass


if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    data_engineer_sample = DataEngineerSample()
    data_engineer_sample.process_header()
    data_engineer_sample.process_data()
    data_engineer_sample.write_data_engineer_sample()
    print('Done the ETL process...')
