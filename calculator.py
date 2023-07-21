#Python calculator with gui

#import everything from tkinter
from tkinter import *

#globally declare the expression variable
expression = ""

#function to update expression
def press(num):

    global expression
    #concatenation of string
    expression = expression + str(num)

    #update the expression using set method
    equation.set(expression)

#function to evaluate expression
def evaluate():
    #try and except handling errors like division by zero etc.
    try:
        global expression
        #evaluate function then convert into string
        total = str(eval(expression))
        equation.set(total)
        #initialize the expression by empty string
        expression = total
    except:
        equation.set(" error ")
        expression = ""

#function to clear the content of text entry box
def clearall():
    global expression
    expression = ""
    equation.set("")
    # expression_field.delete(0, END)

def clearone():
    global expression
    # expression = ""
    # equation.set("")
    txt = equation.get()[:-1]
    equation.set(txt)
    expression = txt
    
#driver code
if __name__ == "__main__":
    #create a GUI window
    gui = Tk()

    #set the background color of GUI window
    gui.configure(background = "#73C6B6")

    #set the title of the GUI
    gui.title("Simple Calculator")

    #set window size
    gui.geometry("250x180")

    #create instance of StringVar class
    equation = StringVar()
    
    #display the expression
    expression_field = Entry(gui, textvariable= equation, bg='powder blue', font=('arial',16))

    #the table has 4 columns
    expression_field.grid(columnspan=4)

    #create buttons
    button1 = Button(gui, text=' 1 ', fg='black', bg='yellow', 
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0) 
    
    button2 = Button(gui, text=' 2 ', fg='black', bg='yellow',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='yellow',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='yellow',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='yellow',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='yellow',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='yellow',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='yellow',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='yellow',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='yellow',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='yellow',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='yellow',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='yellow',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='yellow',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    open = Button(gui, text=' ( ', fg='black', bg='yellow',
                    command=lambda: press("("), height=1, width=7)
    open.grid(row=5, column=1)

    close = Button(gui, text=' ) ', fg='black', bg='yellow',
                    command=lambda: press(")"), height=1, width=7)
    close.grid(row=5, column=2)

    equal = Button(gui, text=' = ', fg='black', bg='yellow',
                command=evaluate, height=1, width=7)
    equal.grid(row=6, column=3, columnspan=1)
 
    clear1 = Button(gui, text=' Clear ', fg='black', bg='yellow',
                    command=clearone , height=1, width=7)
    clear1.grid(row=6, column=1) 
    clear = Button(gui, text='AC', fg='black', bg='yellow',
                command=clearall, height=1, width=7)
    clear.grid(row=6, column=0)
 
    Decimal= Button(gui, text='.', fg='black', bg='yellow',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=2)
    
    # start the GUI
    gui.mainloop()