
from tkinter import *


def press_button(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)



def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ''
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ''
    equation_label.set(equation_text)



window = Tk()
window.title("Calculator program")
window.config(background="turquoise")
window.geometry("500x500")
window.resizable(width=False,height=False)

equation_label = StringVar()
equation_text = ''

label = Label(window, width=24, height=2,bg='#1a300c', font=("consolas",20),textvariable=equation_label, fg="white")
label.pack()

frame = Frame(window)
frame.pack()
button1 = Button(frame,text="1", width=9, height=4,font=34,command=lambda: press_button(1)).grid(row=0,column=0)
button2 = Button(frame,text="2", width=9, height=4,font=34,command=lambda: press_button(2)).grid(row=0,column=1)
button3 = Button(frame,text="3", width=9, height=4,font=34,command=lambda: press_button(3)).grid(row=0,column=2)
button4 = Button(frame,text="4", width=9, height=4,font=34,command=lambda: press_button(4)).grid(row=1,column=0)
button5 = Button(frame,text="5", width=9, height=4,font=34,command=lambda: press_button(5)).grid(row=1,column=1)
button6 = Button(frame,text="6", width=9, height=4,font=34,command=lambda: press_button(6)).grid(row=1,column=2)
button7 = Button(frame,text="7", width=9, height=4,font=34,command=lambda: press_button(7)).grid(row=2,column=0)
button8 = Button(frame,text="8", width=9, height=4,font=34,command=lambda: press_button(8)).grid(row=2,column=1)
button9 = Button(frame,text="9", width=9, height=4,font=34,command=lambda: press_button(9)).grid(row=2,column=2)
button0 = Button(frame,text="0", width=9, height=4,font=34,command=lambda: press_button(0)).grid(row=3,column=0)
plus = Button(frame,text="+", width=9, height=4,font=34,command=lambda: press_button("+")).grid(row=0,column=3)
minus = Button(frame,text="-", width=9, height=4,font=34,command=lambda: press_button("-")).grid(row=1,column=3)
divide = Button(frame,text="/", width=9, height=4,font=34,command=lambda: press_button("/")).grid(row=2,column=3)
times = Button(frame,text="*", width=9, height=4,font=34,command=lambda: press_button("*")).grid(row=3,column=2)
dot = Button(frame,text=".", width=9, height=4,font=34,command=lambda: press_button(".")).grid(row=3,column=1)
equal = Button(frame,text="=", width=9, height=4,font=34,command=equals).grid(row=3,column=3)

clear = Button(window,text="clear", width=14, height=4,font=54,bg="red",fg="white",command=clear).pack()

window.mainloop()

