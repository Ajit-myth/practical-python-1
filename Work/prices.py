import csv

def read_prices(filename):
    p_dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row):
                p_dict.update({row[0]:row[1]})
    return p_dict
