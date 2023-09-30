# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:31:50 2020

@author: mak22
"""


import tkinter as tk
from tkinter import ttk
from tkinter import *

#root = tk.Tk()
'''
def enter_number():#, number):
   # display_text += number
   display_text.set("1")
   display_window.pack()
   root.update()
'''


class Calculator():

   def __init__(self):
        self.root=tk.Tk()
        self.container = ttk.Frame(self.root)
        self.text_buffer =ttk.Label(self.container, text=" ")
        self.display_text = StringVar()
        self.display_text = "0"
        self.currentOp = "none"
        self.numOps = 0
        '''self.num1 = 0
        self.num2 = 0'''
       
        
        def enter_number(number):
            if(self.display_text == '0'):
                clear_screen()
            self.display_text += number
            self.display_window.config(text=self.display_text)            
            self.root.update()
        
        def clear_screen():            
            self.display_text = ''
            self.display_window.config(text='0')          
            self.root.update()
            
        def bt_add():
            self.currentOp = "add"
            if(0 == self.numOps and self.display_text != ''):
                self.num1 = float(self.display_text)
                self.display_window.config(text='+')
                self.display_text = ''
                self.root.update()
        
        def bt_equals():
            if(self.display_text != ''):
                self.num2 = float(self.display_text)
                if(self.currentOp == "add"):
                    self.display_window.config(text=self.num1+self.num2)
                elif(self.currentOp == "subtract"):
                    self.display_window.config(text=self.num1-self.num2)
                elif(self.currentOp == "multiply"):
                    self.display_window.config(text=self.num1*self.num2)
                elif(self.currentOp == "divide"):
                    if(self.num2 != 0):
                        self.display_window.config(text=self.num1/self.num2)
                    else:
                        self.display_window.config(text="ERROR")
                self.display_text = ''
                self.root.update()
                
        def bt_subtract():  
            self.currentOp = "subtract"
            if(0 == self.numOps and self.display_text != ''):
                self.num1 = float(self.display_text)
                self.display_window.config(text='-')
                self.display_text = ''
                self.root.update()
                
        def bt_multiply():  
            self.currentOp = "multiply"
            if(0 == self.numOps and self.display_text != ''):
                self.num1 = float(self.display_text)
                self.display_window.config(text='*')
                self.display_text = ''
                self.root.update()
        
        def bt_divide():
            self.currentOp = "divide"
            if(0 == self.numOps and self.display_text != ''):
                self.num1 = float(self.display_text)
                self.display_window.config(text='/')
                self.display_text = ''
                self.root.update()
            

        self.display_window =ttk.Label(self.container, text=self.display_text) #textvariable=display_text)#
        
        self.bt1 = ttk.Button(self.container, text='1', command=lambda : enter_number('1')) #command=enter_number)#
        self.bt2 = ttk.Button(self.container, text='2', command=lambda : enter_number('2'))
        self.bt3 = ttk.Button(self.container, text='3', command=lambda : enter_number('3'))
        self.bt4 = ttk.Button(self.container, text='4', command=lambda : enter_number('4'))
        self.bt5 = ttk.Button(self.container, text='5', command=lambda : enter_number('5'))
        self.bt6 = ttk.Button(self.container, text='6', command=lambda : enter_number('6'))
        self.bt7 = ttk.Button(self.container, text='7', command=lambda : enter_number('7'))
        self.bt8 = ttk.Button(self.container, text='8', command=lambda : enter_number('8'))
        self.bt9 = ttk.Button(self.container, text='9', command=lambda : enter_number('9'))
        self.bt0 = ttk.Button(self.container, text='0', command=lambda : enter_number('0'))
    
        self.bt_plus = ttk.Button(self.container, text='+', command=lambda : bt_add())
        self.bt_minus = ttk.Button(self.container, text='-', command=lambda : bt_subtract())
        self.bt_mult = ttk.Button(self.container, text='*', command=lambda : bt_multiply())
        self.bt_div = ttk.Button(self.container, text='/', command=lambda : bt_divide())
        self.bt_equals = ttk.Button(self.container, text='=', command=lambda : bt_equals())
        self.bt_clear = ttk.Button(self.container, text='C', command=lambda : clear_screen())
        
        self.container.grid(column=0, row=0)
        self.text_buffer.grid(column=0, row=0)
        self.display_window.grid(column=3, row=1)
        
        
        self.bt_clear.grid(column=0, row=6)
        self.bt_div.grid(column=3, row=3)
        
        
        self.bt7.grid(column=0, row=3)
        self.bt8.grid(column=1, row=3)
        self.bt9.grid(column=2, row=3)
        self.bt_mult.grid(column=3, row=4)
        
        self.bt4.grid(column=0, row=4)
        self.bt5.grid(column=1, row=4)
        self.bt6.grid(column=2, row=4)
        self.bt_minus.grid(column=3, row=5)
        
        
        self.bt1.grid(column=0, row=5)
        self.bt2.grid(column=1, row=5)
        self.bt3.grid(column=2, row=5)
        self.bt_plus.grid(column=3, row=6)
        
        
        #bt_clear.grid(column=0, row=5)
        self.bt0.grid(column=1, row=6)
        self.bt_equals.grid(column=2, row=6)
        #bt_plus.grid(column=2, row=5)
        
        

        
calculator = Calculator()       
calculator.root.mainloop()