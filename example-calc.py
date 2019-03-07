from tkinter import *
from tkinter import messagebox, Button
from time import *

wn = Tk()
wn.geometry("244x440")
wn.configure(background="black")

blank = Entry(wn,background="orange", foreground="black")
blank.insert(0,"")
blank.grid(rowspan=1,columnspan=5,padx=5,pady=30)

calc = 0.0
math_op = ''

def numbtn(value):
    if value != 'C':
        content = blank.get() + value
        blank.delete(0,END)
        blank.insert(0,content)
    elif value == '.':
        content2 = str(blank.get()) + '.'
        blank.insert(0,content2)
    else:
        blank.delete(0,END)

def reverse(value):
    if value == '+':
        reverse = str(blank.get())
        blank.delete(0, END)
        content3 = str("+") + reverse
        blank.insert(0, content3)
    elif value == '-':
        reverse = str(blank.get())
        blank.delete(0, END)
        content4 = str("-") + reverse
        blank.insert(0, content4)


def process(condition):
    global calc
    global math_op
    if condition != '=':
        calc = float(blank.get())
        blank.delete(0,END)

    if condition == '+':
        math_op = '+'
    elif condition == '-':
        math_op = '-'
    elif condition == '*':
        math_op = '*'
    elif condition == '/':
        math_op = '/'
    elif condition == '=':
        if math_op == '+':
            result = calc + float(blank.get())
        elif math_op == '-':
            result = calc - float(blank.get())
        elif math_op == '*':
            result = calc * float(blank.get())
        elif math_op == '/':
            result = calc / float(blank.get())
        blank.delete(0, "end")
        if math_op != '':
            blank.insert(0, str(result))


btn1 = Button(text="1",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('1'))
btn1.grid(row=2,column=0)

btn2 = Button(text="2",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('2'))
btn2.grid(row=2,column=1)

btn3 = Button(text="3",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('3'))
btn3.grid(row=2,column=2)

btn0 = Button(text="0",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('0'))
btn0.grid(row=5,column=0)

btn4 = Button(text="4",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('4'))
btn4.grid(row=3,column=0)

btn5 = Button(text="5",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('5'))
btn5.grid(row=3,column=1)

btn6 = Button(text="6",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('6'))
btn6.grid(row=3,column=2)

btn7 = Button(text="7",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('7'))
btn7.grid(row=4,column=0)

btn8 = Button(text="8",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('8'))
btn8.grid(row=4,column=1)

btn9 = Button(text="9",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('9'))
btn9.grid(row=4,column=2)

btn00 = Button(text="00",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('00'))
btn00.grid(row=5,column=1)

btnTopla = Button(text="+",font="Verdana 10 bold",height="3",width="3",bd=4,background="#E39F29",command=lambda: process("+"))
btnTopla.grid(row=3,column=3)

btnSub = Button(text="-",font="Verdana 10 bold",height="3",width="3",bd=4,background="#E39F29",command=lambda: process(str('-')))
btnSub.grid(row=4,column=3)

btnCarp = Button(text="*",font="Verdana 10 bold",height="3",width="3",bd=4,background="#E39F29",command=lambda: process(str('*')))
btnCarp.grid(row=2,column=3)

btnDiv = Button(text="/",font="Verdana 10 bold",height="3",width="3",bd=4,background="#E39F29",command=lambda: process(str('/')))
btnDiv.grid(row=1,column=3)

btnClear = Button(text="AC",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#495438",command=lambda: numbtn('C'))
btnClear.grid(row=1,column=0)

btnEqual = Button(text="=",font="Verdana 10 bold",height="3",width="3",bd=4,background="#E39F29",command=lambda: process('='))
btnEqual.grid(row=5,column=3)

btnDot = Button(text=".",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#4D4D4D",command=lambda: numbtn('.'))
btnDot.grid(row=5,column=2)

btnpm = Button(text="Minus",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#495438",command=lambda: reverse("-"))
btnpm.grid(row=1,column=1)

btnpm = Button(text="Plus",fg="white",font="Verdana 10 bold",height="3",width="3",bd=4,background="#495438",command=lambda: reverse("+"))
btnpm.grid(row=1,column=2)


wn.mainloop()
