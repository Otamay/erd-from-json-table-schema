"""
Create an ERD from a JSON Table Schema in SVG format.
"""

import sys
sys.path.append('..')
sys.path.append('../..')  # path to pg_jts

from pg_jts import pg_jts
import jts_erd

import json


def main(filename):
    """
    Generate an entity-relationship diagram for the given database.

    filename must be the path to a JSON Table Schema file
    """
    relation_regexps = [
        '(^| )[Rr]ef to ',
        '(^| )[Rr]eference( to|s) ',
    ]
    exclude_tables_regexps = [
        '^tmp_.*$',
        '^temp_.*$',
        '^loc_.*$',
        '^tmp1_.*$',
        '^unused_.*$',
        '^studytmp_.*$',
    ]
    
    with open(filename, 'r') as f:
        j = json.load(f)
    
    notifications = []
    from pprint import pprint as print_
    print_(j, width=200)
    jts_erd.save_svg(
        j,
        'jts_erd_tmp.svg',
        display_columns=True,
        display_indexes=True,
        rankdir='RL',
    )
    for n in notifications:
        print(n[0], n[1])

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        sys.exit("Please supply a filename");
    else:
        filename = sys.argv[1]
    main(filename)
    print('Please find the output in jts_erd_tmp.svg and view it in your browser.')
