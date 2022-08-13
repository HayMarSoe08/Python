# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:07:32 2020

@author: haymarsoe
"""

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.first_top_frame = tkinter.Frame(self.main_window)
        self.second_top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.num1_label = tkinter.Label(self.first_top_frame,
                                        text = "Enter 1st number  : ")

        self.num1_entry = tkinter.Entry(self.first_top_frame,
                                        width = 5)
        
        self.num2_label = tkinter.Label(self.second_top_frame,
                                        text = "Enter 2nd number : ")

        self.num2_entry = tkinter.Entry(self.second_top_frame,
                                        width = 5)
        
        self.num1_label.pack(sid="left")
        self.num1_entry.pack(sid="left")
        self.num2_label.pack(sid="left")
        self.num2_entry.pack(sid="left")
        
        self.descr_label = tkinter.Label(self.mid_frame,
                                          text = 'Result : ')
        self.value = tkinter.IntVar()
        self.result_label = tkinter.Label(self.mid_frame,
                                          textvariable = self.value)
        self.descr_label.pack(sid="left")
        self.result_label.pack(sid="left")
        
        self.add_button = tkinter.Button(self.bottom_frame,
                                          text = " + ",
                                          command = self.add_method)
        self.subtract_button = tkinter.Button(self.bottom_frame,
                                          text = " - ",
                                          command = self.subtract_method)
        self.multiply_button = tkinter.Button(self.bottom_frame,
                                          text = " * ",
                                          command = self.multiply_method)
        self.division_button = tkinter.Button(self.bottom_frame,
                                          text = " / ",
                                          command = self.division_method)        
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = "Quit",
                                          command = self.main_window.destroy)
        
        self.add_button.pack(sid="left")
        self.subtract_button.pack(sid="left")
        self.multiply_button.pack(sid="left")
        self.division_button.pack(sid="left")
        self.quit_button.pack(sid="left")
        
        self.first_top_frame.pack()
        self.second_top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    def add_method(self):
        val1 = int(self.num1_entry.get())
        val2 = int(self.num2_entry.get())
        self.value.set(val1 + val2)
    
    def subtract_method(self):
        val1 = int(self.num1_entry.get())
        val2 = int(self.num2_entry.get())
        self.value.set(val1 - val2)
        
    def multiply_method(self):
        val1 = int(self.num1_entry.get())
        val2 = int(self.num2_entry.get())
        self.value.set(val1 * val2)
        
    def division_method(self):
        val1 = int(self.num1_entry.get())
        val2 = int(self.num2_entry.get())
        self.value.set(val1 / val2)
             
gui = MyGUI()