# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0 #crap, I am not using it as generic parm
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months = months + 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        extra_payment = 1000.0   # This is the place where this can be made generic
    else:
        extra_payment = 0.0
        
    if principal < (payment + extra_payment):
        total_paid = total_paid + principal
        principal = -0.001
    else:
        total_paid = total_paid + payment + extra_payment       
        principal = principal * (1+rate/12) - (payment + extra_payment)
        
    print(months, round(total_paid,2), round(principal,2))
    print(f"Installment number ")
      #:\
      #    Total amount paid = {total_paid:0.2f} \
      #    Remaining principal amount = {principal:0.2f}'
    #print(s)
 

print('Months=',months)
print('Total Paid=', total_paid)
