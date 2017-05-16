#!/usr/bin/python3
"""
Take a csv file and draw the shape of all residuts (must be named res_<carac>).

Usage:
    ./shape_res.py <file>

Options:
    -h, --help      Show this screen
    -v, --version   Show script version

"""

##########
# IMPORT #
##########
import os

import pandas as pd
import numpy
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from docopt import docopt

########
# MAIN #
########
def res_shape_drawing(args):
    doc_name  = args['<file>']
    res_dir   = 'res_'+(doc_name.split('.')[0])
    # Import of the csv file
    print("Importing data")
    dt = pd.read_csv(doc_name)

    # Selection of residuts column
    residuts = [col for col in dt.columns if col[:3] == 'res']

    # Create the result directory
    if res_dir not in os.listdir():
        print("Creation of result directory: " + res_dir)
        os.mkdir(res_dir)

    # Draw the graphs
    for res in residuts:
        print("Drawing the " + res + " graph")
        dt[res].plot(kind='density')
        # Hide Y axis
        # frame = plt.gca()
        # frame.axes.get_yaxis().set_visible(False)
        plt.savefig(res_dir + '/' + res + '_qo_A3_CI.png')
        plt.close()

##########
# LAUNCH #
##########
if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.1')
    res_shape_drawing(arguments)
