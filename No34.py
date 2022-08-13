# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:30:25 2020

@author: haymarsoe
"""
import matplotlib.pyplot as plt
def main():
    expensefile = open('myexpenses.txt', 'w')

    expensefile.write(input("Enter your Rent expense: ") + '\n')
    expensefile.write(input("Enter your Gas expense: ") + '\n')
    expensefile.write(input("Enter your Food expense: ") + '\n')
    expensefile.write(input("Enter your Clothing expense: ") + '\n')
    expensefile.write(input("Enter your Donation expense: ") + '\n')
    expensefile.write(input("Enter your Misc expense: ") + '\n')
    
    expensefile.close()
    
    print('your last month expenses ..')
    
    infile = open('myexpenses.txt', 'r')
    data = infile.readlines()

    for i in infile:
        data[i] = infile.readline().rstrip('\n')
    
    slice_labels = ["Rent", "Gas","Food","Clothing", "Donation", "Misc"]
    
    plt.pie(data,labels=slice_labels,colors = ('g','m','y','c','r','b'))
    
    plt.title('Last Month Expenses')    
   
    #Dsipay the pie chart
    plt.show()

main()


