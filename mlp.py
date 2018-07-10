import tensorflow as tensorflow
import argparse
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import csv

def read_data(config):
    print('Reading data... \n')
    data = []
    with open(config.data, 'rt') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in data_reader:
            data.append(row)


def read_params():
    parser = argparse.ArgumentParser()
    data = parser.add_argument_group('data')
    
    data.add_argument('--data', type=str, metavar='PATH',
                  help="data")
    config = parser.parse_args()
    
    if not config.data:
        logging.error('argument needed: --data should be provided.')
        sys.exit(1)

    return config

def main():
    config = read_params()
    data = read_data(config)


main()
