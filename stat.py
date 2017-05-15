#!/usr/bin/python3
"""
Explanations

Usage:
    ./stat.py <data.csv>

Options:
    -h, --help      Show this screen
    -v, --version   Show version
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
    data = pd.read_csv(args["<data.csv>"]).groupby("Lot")
    data.describe().to_csv("stats_"+args["<data.csv>"])

#############
# FUNCTIONS #
#############

##########
# LAUNCH #
##########
if __name__ == "__main__":
    arguments = docopt(__doc__, version="1.0.0")
    main(arguments)
