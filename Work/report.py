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
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            p_dict = dict(zip(header,row))
            #p_list = list(zip(p_dict.keys(), p_dict.values()))
           # p_dict = {'Name':row[0], 'Shares':int(row[1]), 'Price':float(row[2])}
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
        if n['name'] in prices:
           # chg = float(prices.get(n['name'], 0.0)) - n['price']
            chg = float((prices.get(n['name'], 0))) - float(n['price'])
           #result = {**n, **{'Change':chg}} #append the existing dict
            report.append((n['name'], n['shares'], n['price'], chg))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + " ") * len(headers))
    for r in report:
         print('%10s %10s %10s %10.2f' % r)


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)    
    
    
