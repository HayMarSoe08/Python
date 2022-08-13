# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:10:37 2020

@author: haymarsoe
"""

class Invoice:
    def __init__(self, number, description, quantity, price):
        self.number = number;
        self.description = description;
        self.quantity = quantity
        self.price = price
        
    def calculate_invoice(self):
        amount = 0
        if(self.quantity > 0 and self.price > 0):        
            amount = self.quantity * self.price
        else:
            print()
            print("Invalid Quantity & Price..")            
        return amount
        
def main():
    number = input("Enter Number :")
    description = input("Enter Description :")
    quantity = float(input("Enter Quantity of item :"))
    price = float(input("Enter Price per item :"))
    data = Invoice(number, description, quantity, price)
    if(data.calculate_invoice()):
        print()
        print("---Invoice--- ")
        print("Invoice Number :", data.number)
        print("Invoice Description :", data.description)
        print("Quantity of item :", data.quantity)
        print("Price per item :", data.price)
        print("Invoice Amount :", data.calculate_invoice())

main = main()