import tkinter as tk
from tkinter import *
import math as mt
pi=3.14159265359
result=0
mainWindow=tk.Tk()
mainWindow.title("SCIENTIFIC CALCULATOR")
mainWindow.configure(background="white")
mainWindow.geometry("580x540")
heading_label=tk.Label(mainWindow,text="ENTER FIRST NUMBER")
heading_label.grid(row=0,columnspan=4, sticky=W+E)
first_field=tk.Entry(mainWindow)
first_field.grid(row=1,columnspan=4, sticky=W+E)
heading_label=tk.Label(mainWindow,text="ENTER SECOND NUMBER")
heading_label.grid(row=2,columnspan=4, sticky=W+E)
second_field=tk.Entry(mainWindow)
second_field.grid(row=3,columnspan=4, sticky=W+E)
operation=tk.Label(mainWindow,text="operator")
operation.grid(row=4,columnspan=4, sticky=W+E)
result_label=tk.Label(mainWindow, text="operations result is:")
result_label.grid(row=10,columnspan=4, sticky=W+E)
equation = StringVar() 

def addition():
    first=int(eval(first_field.get()))
    second=int(eval(second_field.get()))
    result=first+second
    result_label.config(text="" +str(result)).grid(row=10,columnspan=4, sticky=W+E)
addition_button=tk.Button(mainWindow,text="+",fg='black', bg='light grey',command=lambda:addition(),height=2, width=7) 
addition_button.grid(row=5, column=0,ipadx=40)



def minus():
    first=int(eval(first_field.get()))
    second=int(eval(second_field.get()))
    result=first-second
    result_label.config(text="" +str(result))
minus_button=tk.Button(mainWindow,text="-", fg='black', bg='light grey', command=lambda:minus(),height=2, width=7)
minus_button.grid(row=5, column=1,ipadx=40)


def multiply():
    first=int(eval(first_field.get()))
    second=int(eval(second_field.get()))
    result=first*second
    result_label.config(text="" +str(result))
mul_button=tk.Button(mainWindow,text="*", fg='black', bg='light grey',command=lambda:multiply(),height=2, width=7)
mul_button.grid(row=5, column=2,ipadx=40)


def divide():
    first=int(eval(first_field.get()))
    second=int(eval(second_field.get()))
    result=first/second
    result_label.config(text="" +str(result))
divide_button=tk.Button(mainWindow,text="/", fg='black', bg='light grey',command=lambda:divide(),height=2, width=7)
divide_button.grid(row=5, column=3,ipadx=40)

def sine():
    first=eval(first_field.get())
    result=mt.sin(first)
    result_label.config(text="" +str(result))
sin_button=tk.Button(mainWindow,text="sin",fg='black', bg='light grey', command=lambda:sine(),height=2, width=7)
sin_button.grid(row=6, column=0,ipadx=40)


def cosine():
    first=eval(first_field.get())
    result=mt.cos(first)
    result_label.config(text="" +str(result))
cos_button=tk.Button(mainWindow,text="cos", fg='black', bg='light grey',command=lambda:cosine(),height=2, width=7)
cos_button.grid(row=6, column=1,ipadx=40)



def tan():
    first=eval(first_field.get())
    result=mt.tan(first)
    result_label.config(text="" +str(result))
tan_button=tk.Button(mainWindow,text="tan",fg='black', bg='light grey', command=lambda:tan(),height=2, width=7)
tan_button.grid(row=6, column=2,ipadx=40)


def atan2():
    first=eval(first_field.get())
    second=eval(second_field.get())
    result=mt.atan2(float(second), float(first))
    result_label.config(text="" +str(result))
atan2_button=tk.Button(mainWindow,text="atan2",fg='black', bg='light grey', command=lambda:atan2(),height=2, width=7)
atan2_button.grid(row=6, column=3,ipadx=40)

def asine():
    first=eval(first_field.get())
    result=mt.asin(first)
    result_label.config(text="" +str(result))
asin_button=tk.Button(mainWindow,text="asin",fg='black', bg='light grey', command=lambda:asine(),height=2, width=7)
asin_button.grid(row=7, column=0,ipadx=40)


def acosine():
    first=eval(first_field.get())
    result=mt.acos(first)
    result_label.config(text="" +str(result))
acos_button=tk.Button(mainWindow,text="acos", fg='black', bg='light grey',command=lambda:acosine(),height=2, width=7)
acos_button.grid(row=7, column=1,ipadx=40)


def atan():
    first=eval(first_field.get())
    result=mt.atan(first)
    result_label.config(text="" +str(result))
atan_button=tk.Button(mainWindow,text="atan",fg='black', bg='light grey', command=lambda:atan(),height=2, width=7)
atan_button.grid(row=7, column=2,ipadx=40)


def deg():
    first=eval(first_field.get())
    result=(float(first) * 180)/pi
    result_label.config(text="" +str(result))
deg_button=tk.Button(mainWindow,text="deg",fg='black', bg='light grey', command=lambda:deg(),height=2, width=7)
deg_button.grid(row=8, column=0,ipadx=40)


def rad():
    first=eval(first_field.get())
    result=(float(first) * pi)/180
    result_label.config(text="" +str(result))
rad_button=tk.Button(mainWindow,text="rad",fg='black', bg='light grey', command=lambda:rad(),height=2, width=7)
rad_button.grid(row=8, column=1,ipadx=40)

def root():
    first=float(eval(first_field.get()))
    second=float(second_field.get())
    result=first**(1/second)
    result_label.config(text="" +str(result))
root_button=tk.Button(mainWindow,text="root",fg='black', bg='light grey', command=lambda:root(),height=2, width=7)
root_button.grid(row=8, column=2,ipadx=40)

def equalpress():
    result =eval(str(first_field.get()))
    result_label.config(text="" +str(result)).grid(row=10,columnspan=4, sticky=W+E)
equal_button=tk.Button(mainWindow, text=' = ', fg='black', bg='light grey',command=lambda:equalpress(), height=2, width=7)
equal_button.grid(row=8, column=3,ipadx=40)

def clear():
    result_label.config(text="" +str(result))
equ_button=tk.Button(mainWindow,text="Del result",fg='black', bg='light grey', command=lambda:clear(),height=2, width=7)
equ_button.grid(row=7, column=3,ipadx=40)

def pow():
    first=eval(first_field.get())
    second=eval(second_field.get())
    result=mt.pow(float(first), float(second))
    result_label.config(text="" +str(result))
pow_button=tk.Button(mainWindow,text="pow",fg='black', bg='light grey', command=lambda:pow(),height=2, width=7)
pow_button.grid(row=9, column=0,ipadx=40)


def hypot():
    first=eval(first_field.get())
    second=eval(second_field.get())

    result=mt.hypot(float(first), float(second))
    result_label.config(text="" +str(result))
hypot_button=tk.Button(mainWindow,text="hypot",fg='black', bg='light grey', command=lambda:hypot(),height=2, width=7)
hypot_button.grid(row=9, column=1,ipadx=40)

def log():
    first=eval(first_field.get())
    second=eval(second_field.get())
    if(second == 0):
        result=mt.log(10,first)
    else:
        result=mt.log(second,first)
    result_label.config(text="" +str(result))
log_button=tk.Button(mainWindow,text="log",fg='black', bg='light grey', command=lambda:log(),height=2, width=7)
log_button.grid(row=9, column=2,ipadx=40)

def fact():
    result=mt.factorial(eval(first_field.get()))
    result_label.config(text="" +str(result))
fact_button=tk.Button(mainWindow,text="fact",fg='black', bg='light grey', command=lambda:fact(),height=2, width=7)
fact_button.grid(row=9, column=3,ipadx=40)



mainWindow.mainloop()
