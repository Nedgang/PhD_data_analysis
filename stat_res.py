#!/usr/bin/python3
"""
Take a csv file and calculate the means of all residus group by father id

Usage:
    ./shape_res.py <file> --output=<file>

Options:
    -h, --help              Show this screen
    -o, --output=<file>     Output file
    -v, --version           Show script version

"""

##########
# IMPORT #
##########
import pandas as pd

from docopt import docopt

########
# MAIN #
########
def res_shape_drawing(args):
    doc_name  = args['<file>']
    output   = args["--output"]
    # Import of the csv file
    print("Importing data")
    dt = pd.read_csv(doc_name)

    # Selection of residus column
    residus = [col for col in dt.columns if col[:3] == 'res']

    return_dataframe = pd.DataFrame()

    grouped_dataframe = dt.groupby("IDMere")

    # Mean residus individualy
    return_dataframe["mean_res_po"] = grouped_dataframe["res_poids"].mean()
    return_dataframe["mean_res_lab"] = grouped_dataframe["res_lab"].mean()
    return_dataframe["mean_res_ff"] = grouped_dataframe["res_ff"].mean()
    return_dataframe["mean_res_de"] = grouped_dataframe["res_de"].mean()
    return_dataframe["mean_res_in"] = grouped_dataframe["res_in"].mean()
    return_dataframe["mean_res_di"] = grouped_dataframe["res_di"].mean()
    return_dataframe["mean_res_ha"] = grouped_dataframe["res_ha"].mean()
    return_dataframe["mean_res_uh"] = grouped_dataframe["res_uh"].mean()
    return_dataframe["mean_res_si"] = grouped_dataframe["res_si"].mean()

    # Mean residus by groups
    return_dataframe["mean_res_coq"] = return_dataframe.apply(mean_coq, axis=1)
    return_dataframe["mean_res_int"] = return_dataframe.apply(mean_int, axis=1)

    # Mean residus for all
    return_dataframe["mean_all_res"] = return_dataframe.apply(mean_all, axis=1)

    return_dataframe.to_csv(output)
    # print(return_dataframe)

#############
# FUNCTIONS #
#############
def mean_coq(row):
    return (row["mean_res_lab"] + row["mean_res_ff"] + row["mean_res_de"] +\
            row["mean_res_di"] + row["mean_res_si"])/5

def mean_int(row):
    return (row["mean_res_po"] + row["mean_res_in"] + row["mean_res_ha"] +\
            row["mean_res_uh"])/4

def mean_all(row):
    return (row["mean_res_po"] + row["mean_res_in"] + row["mean_res_ha"] +\
            row["mean_res_uh"]+\
            row["mean_res_lab"] + row["mean_res_ff"] + row["mean_res_de"] +\
            row["mean_res_di"] + row["mean_res_si"])/9

#########u
# LAUNCH #
##########
if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.1')
    res_shape_drawing(arguments)
