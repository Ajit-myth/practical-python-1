# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename):
    Total = 0.0
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers,row))
            try:
                #print(rowno, row)
                price = float(record['price'])
                nshares = int(record['shares'])
#                linelist = line.split(',')
#                ShareValue = linelist[2].split('\n')[0]
#                intValue = float(ShareValue)
#                NumShares = float(linelist[1])
                Total = Total + nshares*price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return Total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total cost = ', cost)
