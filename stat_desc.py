#!/usr/bin/python3
"""
Script used to determine the number of descendants by hens.

Usage:
    ./filiation.py <data.csv> --output=<out.csv>

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
    data   = pd.read_csv(args['<data.csv>'])
    # Use of a dictionnary of set to stock the infos
    # Format: result = {id1:{A, B}, id2:{C, D}}
    result = {}

    print("Détermination du nombre de descendants par individus\n")
    for i, row in data.iterrows():
        fath_id = row['IDPere']
        if not pd.isnull(fath_id):
            if fath_id not in result:
                if row['Type_cage'] == 'individuelle':
                    type_cage = 'individuelle'
                    result[fath_id] = {row['BirdID']}
                else:
                    type_cage = 'multiple'
                    result[fath_id] = {row['Cage']}
            else:
                if row['Type_cage'] == 'individuelle':
                    result[fath_id].add(row['BirdID'])
                else:
                    result[fath_id].add(row['Cage'])


    print("Nombre de pères identifiés:", len(result))
    if type_cage == 'individuelle':
        for pere in result:
            result[pere] = len(result[pere])

        enough_desc_fath = [fath for fath in result if result[fath] >= 10]
        print("Pères avec une descendance >= 10 individus:", len(enough_desc_fath))
    else:
        for pere in result:
            result[pere] = len(result[pere])*5
        enough_desc_fath = [fath for fath in result if result[fath] >= 10]
        print("Pères avec une descendance >= 10 individus:", len(enough_desc_fath))

    result_df = pd.DataFrame.from_dict(result, orient='index')

    result_df.index.names = ['ID_father']
    result_df.index = result_df.index.astype(int)

    result_df.columns = ['Descendants_number']
    result_df.sort_values(by='Descendants_number')

    print(
        "Nombre moyen de filles par père:",
        result_df['Descendants_number'].mean(),
        '\n'
    )

    print("Saving results in:", args['--output'])
    result_df.to_csv(args['--output'])

#############
# FUNCTIONS #
#############

##########
# LAUNCH #
##########
if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0')
    main(arguments)
