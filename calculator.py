from tkinter import *
from math import *
import tkinter.font as font
root = Tk()
root.title('                          Calculator')
root.geometry('300x400')
root.resizable(False, False)
top = Frame(root)
top.pack()
Font1 = font.Font(family='Helvetica', size=15)
Font2 = font.Font(family='TimeNewRoman' , size = 20)


input = Text(top,  height=1, width=100, bg="light green" , font = Font2)
input.pack()

def operation():

        INPUT = input.get("1.0", "end-1c") #Takes input from display
        length = len(INPUT)
        print(INPUT) #Prints it on the screen for validation
        INPUT = INPUT.replace("^" , "**")

        input.delete('1.0', END)#Deletes the past input




        input.insert(END, eval(INPUT))#Inserts the new evaluated answer , eval takes string and turns it into an operation

def fullclear():
    input.delete('1.0', END)



INPUT = ""


########################Oparators######################
def faddition(input, add):
    input.insert(END, add)


def fsubstraction(input, sub):
    input.insert(END, sub)


def fdivission(input, div):
    input.insert(END, div)


def fmultiplication(input, mul):
    input.insert(END, mul)


def fmodulus(input, mod):
    input.insert(END, mod)


def fexponent(input, ex):
    input.insert(END, ex)


def fequals(input, eq):
    input.insert(END, eq)

def froot(input, root):
    input.insert(END , root)

def rparenthesis(input, rpar):
    input.insert(END , rpar)

def lparenthesis(input, lpar):
    input.insert(END , lpar)

def fsin(input, sin):
    input.insert(END , sin)

def fcos(input, cos):
    input.insert(END , cos)

def ftan(input, tan):
    input.insert(END , tan)
########################################################
########################## Numbers ############################


def num0(input, num0):
    input.insert(END, num0)


def num1(input, num1):
    input.insert(END, num1)


def num2(input, num2):
    input.insert(END, num2)


def num3(input, num3):
    input.insert(END, num3)


def num4(input, num4):
    input.insert(END, num4)


def num5(input, num5):
    input.insert(END, num5)


def num6(input, num6):
    input.insert(END, num6)


def num7(input, num7):
    input.insert(END, num7)


def num8(input, num8):
    input.insert(END, num8)


def num9(input, num9):
    input.insert(END, num9)

def dec(input, dec):
    input.insert(END, dec)
##############################################################
####################NUMBER BUTTONS###################################
number0= Button(root, text='0', width=5, height=1, command=lambda: num0(input, "0"))
number0.place(x=80, y=250)
number0['font'] = Font1

number1= Button(root, text='1', width=5, height=1, command=lambda: num1(input, "1"))
number1.place(x=10, y=100)
number1['font'] = Font1

number2= Button(root, text='2', width=5, height=1, command=lambda: num2(input, "2"))
number2.place(x=80, y=100)
number2['font'] = Font1

number3= Button(root, text='3', width=5, height=1, command=lambda: num3(input, "3"))
number3.place(x=150, y=100)
number3['font'] = Font1

number4= Button(root, text='4', width=5, height=1, command=lambda: num4(input, "4"))
number4.place(x=10, y=150)
number4['font'] = Font1

number5= Button(root, text='5', width=5, height=1, command=lambda: num5(input, "5"))
number5.place(x=80, y=150)
number5['font'] = Font1

number6= Button(root, text='6', width=5, height=1, command=lambda: num6(input, "6"))
number6.place(x=150, y=150)
number6['font'] = Font1

number7= Button(root, text='7', width=5, height=1, command=lambda: num7(input, "7"))
number7.place(x=10, y=200)
number7['font'] = Font1

number8= Button(root, text='8', width=5, height=1, command=lambda: num8(input, "8"))
number8.place(x=80, y=200)
number8['font'] = Font1

number9= Button(root, text='9', width=5, height=1, command=lambda: num9(input, "9"))
number9.place(x=150, y=200)
number9['font'] = Font1

##########################################################################################
########################################OPARATOR BUTTONS##################################

addition = Button(root, text='+', width=5, height=1, command=lambda: faddition(input, "+"))
addition.place(x=220, y=100)
addition['font'] = Font1

subtraction = Button(root, text='-', width=5, height=1, command=lambda: fsubstraction(input, "-"))
subtraction.place(x=220, y=150)
subtraction['font'] = Font1

multiplication = Button(root, text='*', width=5, height=1, command=lambda: fmultiplication(input, "*"))
multiplication.place(x=220, y=200)
multiplication['font'] = Font1

division = Button(root, text='/', width=5, height=1, command=lambda: fdivission(input, "/"))
division.place(x=220, y=250)
division['font'] = Font1

modulus = Button(root, text='%', width=2, height=2, command=lambda: fmodulus(input, "%"))
modulus.place(x=180, y=420)

exponent = Button(root, text='^', width=5, height=1, command=lambda: fexponent(input, "^"))
exponent.place(x=10 , y = 300)
exponent['font'] = Font1

equals = Button(root, text='=', width=5, height=1 , command  = lambda: operation())
equals.place(x=220, y=300)
equals['font'] = Font1

decimal = Button(root, text='.', width=5, height=1, command=lambda: dec(input, "."))
decimal.place(x=10, y=250)
decimal['font'] = Font1

AC = Button(root, text='AC', width=5, height=1, command=lambda: fullclear())
AC.place(x=150, y=250)
AC['font'] = Font1

sroot = Button(root, text="Root", command = lambda: froot(input , "sqrt()") )
sroot.place(x=150, y=300)
sroot['font'] = Font1

rpar = Button(root, text=")", command = lambda: rparenthesis(input , ")") )
rpar.place(x=120, y=300)
rpar['font'] = Font1

lpar = Button(root, text="(", command = lambda: lparenthesis(input , "(") )
lpar.place(x=80, y=300)
lpar['font'] = Font1
#TBD
# sin = Button(root, text="  sin  ", command = lambda: fsin(input , "sin()") )
# sin.place(x=10, y=350)
# sin['font'] = Font1
#
# cos = Button(root, text="  cos  ", command = lambda: fcos(input , "cos()") )
# cos.place(x=120, y=350)
# cos['font'] = Font1
#
# tan = Button(root, text="  tan  ", command = lambda: ftan(input , "tan()") )
# tan.place(x=220, y=350)
# tan['font'] = Font1

root.mainloop()
