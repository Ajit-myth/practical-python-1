# pcost.py
#
# Exercise 1.27
Total = 0
with open('Data/portfolio.csv','rt') as f:
    header = next(f)
    for line in f:
        linelist = line.split(',')
        ShareValue = linelist[2].split('\n')[0]
        intValue = float(ShareValue)
        NumShares = float(linelist[1])
        Total = Total + intValue*NumShares
        
print('Total cost = ',Total)
