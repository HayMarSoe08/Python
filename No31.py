# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 08:39:34 2020

@author: haymarsoe
"""

import tkinter
import random

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.descr_label = tkinter.Label(self.top_frame,
                                        text = 'Your Lottery Number is : ')
        self.value = tkinter.StringVar()
        self.show_label = tkinter.Label(self.top_frame,
                                        textvariable = self.value)
        
        self.descr_label.pack()
        self.show_label.pack()
        
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text = "OK",
                                        command = self.random_method)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = "Quit",
                                          command = self.main_window.destroy)
        
        self.ok_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    def random_method(self):
        result = ""
        for count in range(0, 6):
            val = random.randint(0, 9)
            result = result + str(val)
       
        self.value.set(result)
            
gui = MyGUI()
        
        
        
        
        
        
        