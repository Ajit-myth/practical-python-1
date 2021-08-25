# pcost.py
#
# Exercise 1.27
import sys
def portfolio_cost(filename):
    Total = 0
    with open(filename,'rt') as f:
        next(f)
        for line in f:
            linelist = line.split(',')
            ShareValue = linelist[2].split('\n')[0]
            intValue = float(ShareValue)
            NumShares = float(linelist[1])
            Total = Total + intValue*NumShares
    return Total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total cost = ', cost)
