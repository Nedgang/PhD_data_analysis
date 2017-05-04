#!/usr/bin/python3
"""
Script used to determine the number of descendants by hens.
Use "localisation des troupeaux" files.

Usage:
    ./filiation.py <data> --output=<out.csv>

Options:
    -h, --help              Show this screen
    -o, --output=<file>     Output file
    -v, --version           Show version
"""

##########
# IMPORT #
##########
import pandas as pd

from docopt import docopt

########
# MAIN #
########
def main(args):
    print("Loading file")
    data = pd.read_csv(args["<data>"])

    print("Calculation of the offspring\n")
    count = pd.value_counts(data["ID Père"]).to_frame("Descendants number")

    count.index.names = ["IDPere"]
    count.index= count.index.astype(int)

    print("Mean:", count.mean()[0])
    print("Number of lines:", count.shape[0], "\n")

    print("Writing result file:", args["--output"])
    count.to_csv(args["--output"])


#############
# FUNCTIONS #
#############

##########
# LAUNCH #
##########
if __name__ == "__main__":
    arguments = docopt(__doc__, version="1.0.0")
    main(arguments)
