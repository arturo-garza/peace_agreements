import tensorflow as tensorflow
import argparse
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import csv

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [8, 6]

#Verify
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)


def read_data(config):
    print('Reading data... \n')
    data = pd.read_csv(config.data)

    return data

def model():
    tf.
    # Tf placeholders
    X = tf.placeholder(tf.float32, [None, n_input])
    y = tf.placeholder(tf.float32, [None, n_classes])

    layer1 = tf.nn.dropout(tf.nn.tanh(tf.add(tf.matmul(_X, _weights['h1']), _biases['b1'])), dropout_keep_prob)
    layer2 = tf.nn.dropout(tf.nn.tanh(tf.add(tf.matmul(layer1, _weights['h2']), _biases['b2'])), dropout_keep_prob)
    layer3 = tf.nn.dropout(tf.nn.tanh(tf.add(tf.matmul(layer2, _weights['h3']), _biases['b3'])), dropout_keep_prob)
    layer4 = tf.nn.dropout(tf.nn.tanh(tf.add(tf.matmul(layer3, _weights['h4']), _biases['b4'])), dropout_keep_prob)
    out = ACTIVATION_FUNCTION_OUT(tf.add(tf.matmul(layer4, _weights['out']), _biases['out']))

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
    #print(data.head())
    #print(data.Reg.value_counts())
    #print(data.Con.value_counts())
    sns.countplot(x = 'Reg', data = data)
    plt.show()

main()
