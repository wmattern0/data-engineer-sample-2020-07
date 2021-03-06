import csv
import pathlib
import src.some_storage_library

"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""

class DataEngineerSample:

    def __init__(self):
        self.data_eng_sample_data=''
        self.data_eng_sample_header=''

    def process_header(self):
        header_file = open(pathlib.Path('data/source/SOURCECOLUMNS.txt'))
        header_reader = csv.reader(header_file, delimiter='|')
        header_dict = dict(header_reader)

        # put headers in numeric order, using a dictionary to sort this file
        ordered_keys = sorted(header_dict, key=lambda i: int(i))
        ordered_headers = []
        for i in ordered_keys:
            ordered_headers.append(header_dict.get(i))
        self.data_eng_sample_header = ordered_headers

    def process_data(self):
        data_file = open(pathlib.Path('data/source/SOURCEDATA.txt'))
        data_reader = csv.reader(data_file, delimiter='|')
        self.data_eng_sample_data = list(data_reader)

    def write_data_engineer_sample_output(self):
        writer = src.some_storage_library.SomeStorageLibrary()
        outputFile = open('output.csv', 'w', newline='')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(self.data_eng_sample_header)
        for row in self.data_eng_sample_data:
            outputWriter.writerow(row)
        writer.load_csv('output.csv')


if __name__ == '__main__':
    """Entrypoint"""
    #TODO: make rerunnable when file already exists in landing zone
    print('Beginning the ETL process...')
    data_engineer_sample = DataEngineerSample()
    data_engineer_sample.process_header()
    data_engineer_sample.process_data()
    data_engineer_sample.write_data_engineer_sample_output()
