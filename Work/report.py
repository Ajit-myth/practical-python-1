# report.py
#
# Exercise 2.4
import csv
#portfolio = []
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        p_dict = {}
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            p_dict = {'Name':row[0], 'Shares':int(row[1]), 'Price':float(row[2])}
            portfolio.append(p_dict)
           
    return portfolio


def read_prices(filename):
    p_dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row):
                p_dict.update({row[0]:row[1]})
    return p_dict

def make_report(portfolio, prices):
    report = []
    for n in portfolio:
        if n['Name'] in prices:
            chg = float(prices.get(n['Name'], 0.0)) - n['Price']
           #result = {**n, **{'Change':chg}} #append the existing dict
            report.append((n['Name'], n['Shares'], n['Price'], chg))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + " ") * len(headers))
    for r in report:
         print('%10s %10d %10.2f %10.2f' % r)


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)    
    
    
