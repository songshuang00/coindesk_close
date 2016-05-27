import csv
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import datetime
import math


with open('coindesk-bpi-USD-close.csv', 'rb') as csvfile:
    reader= csv.reader(csvfile)
    n= 0
    for row in reader:
        if '-' in row:
            date[n], price[n] = row.split(',')
            n+= 1

x= np.arange(n+1)
for n in price:
    y[n]= float(price[n])

def predict_price(x, y, n):    
    pf= sp.polyfit(x, y, 5)
    price_t= sp.polyval(pf, n+1)
    return price_t
    
price_t_1= predict_price(x, y, n)
    
print 'The lattest polyfitted result is '+str(price_t_1)+'.\n'

def average_price(i, n, price):
    for m in range(i-1, n+1):
        for p in range(n-i+2):
            for q in range(i):
                sum[p]+= price[m-q]
            average[p]= math.round(sum[p]/i, 2)
    return average

x_5= np.arange(n-3)
y_5= average_price(5, n, price)
price_t_5= predict_price(x_5, y_5, n-3)

print 'The lattest 5-days average is '+str(price_t_5)+'.\n'

x_20= np.arange(n-18)
y_20= average_price(20, n, price)
price_t_20= predict_price(x_20, y_20, n-18)

print 'The lattest 20-days average is '+str(price_t_20)+'.\n'
    
def judge_price(price_t_1, price_t_5, price_t_20):
    if price_t_1>price_t_5 and price_t_5>price_t_20:
        print 'You shall hold bitcoins.'
    elif price_t_1<=price_t_5 and price_t_5>price_t_20:
        print 'You shall buy bitcoins.'
    elif price_t_1>price_t_20 and price_t_5<=price_t_20:
        print 'You shall sell bitcoins.'
    elif price_t_1<=price_t_20 and price_t_5<=price_t_20:  
        print 'You shall hold bitcoins.'
    else:
        break
        
judge_price(price_t_1, price_t_5, price_t_20)

x= sp.linspace(0, 51, 1000)
plt.plot(x, y[n-50:n], linewidth= 4)
plt.plot(x, y_5[n-54:n-4], linewidth= 2)
plt.plot(x, y[n-69:n-19], linewidth= 2)
plt.plot(51, price_t_1, 'or', label='point')
plt.plot(51, price_t_5, 'o', label='point')
plt.plot(51, price_t_20, 'o', label='point')
plt.grid()
plt.show()