import customtkinter
from tkinter import *

root = Tk()
root.title("Calculadora")
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)
root.configure(background="#121212")

# Input
e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#121212', bg="#d6d6d6", font=('futura', 25,'bold'), justify=RIGHT)
e.grid(
    row = 0,
    column = 0,
    columnspan = 3,
    pady= 2,
)

# Funções ------------------------------------------------------

num1 = ''
divisao = FALSE
multiplicacao = FALSE
adicao = FALSE
subtracao = FALSE



def botaoClick(num):
    e.insert(END, num)

def botaoDivisao():
    global num1
    global divisao
    divisao = TRUE
    num1 = e.get()
    e.delete(0, END) 

def botaoMultiplica():
    global num1
    global multiplicacao
    multiplicacao = TRUE
    num1 = e.get()
    e.delete(0, END)  

def botaoSoma():
    global num1
    global adicao
    adicao = TRUE
    num1 = e.get()
    e.delete(0, END)  

def botaoSubtrai():
    global num1
    global subtracao
    subtracao = TRUE
    num1 = e.get()
    e.delete(0, END)  

def botaoApaga():
    global num1
    global num2
    num1 = ''
    num2 = ''
    e.delete(0, END)  

def botaoIgual():
    global subtracao
    global adicao
    global multiplicacao
    global divisao
    
    num2 = e.get()
    e.delete(0, END)

    if subtracao == TRUE:
        e.insert(0, int(num1) - int(num2))
        subtracao = FALSE
    
    if adicao == TRUE:
        e.insert(0, int(num1) + int(num2))
        adicao = FALSE
    
    if multiplicacao == TRUE:
        e.insert(0, int(num1) * int(num2))
        multiplicacao = FALSE
    
    if divisao == TRUE:
        e.insert(0, int(num1) / int(num2))
        divisao = FALSE
    


     



# primeira Coluna

btn7 = Button(root,
                    text='7',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(7),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=1, column=0)

btn4 = Button(root,
                    text='4',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(4),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=2, column=0)

btn1 = Button(root,
                    text='1',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(1),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=3, column=0)

btn0 = Button(root,
                    text='0',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(0),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=4, column=0)

# Segunda Coluna

btn8 = Button(root,
                    text='8',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(8),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=1, column=1)

btn5 = Button(root,
                    text='5',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(5),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=2, column=1)

btn2 = Button(root,
                    text='2',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(2),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=3, column=1)

btnDivisao = Button(root,
                        text='÷',
                        padx=39,
                        pady=20,
                        command=botaoDivisao,
                        fg='#FFFFFF',
                        activeforeground='#d95300',
                        bg='#d95300',
                        activebackground='#FFFFFF',
                        font=('futura',12,'bold'),
                        relief=FLAT
                        ).grid(row=4,column=1)

# Terceira Coluna ----------------------------------------------------------------------------------------------------

btn9 = Button(root,
                    text='9',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(9),
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=1, column=2)

btn6 = Button(root,
                    text='6',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(6),
                    fg='#FFFFFF',
                    activeforeground='#121212',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=2, column=2)

btn3 = Button(root,
                    text='3',
                    padx=40,
                    pady=20,
                    command=lambda: botaoClick(3),
                    fg='#FFFFFF',
                    activeforeground='#121212',
                    bg='#121212',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=3, column=2)

btnMultiplica = Button(root,
                        text='X',
                        padx=50,
                        pady=20,
                        command=botaoMultiplica,
                        fg='#FFFFFF',
                        activeforeground='#d95300',
                        bg='#d95300',
                        activebackground='#FFFFFF',
                        font=('futura',12,'bold'),
                        relief=FLAT
                        ).grid(row=4, column=2)


# Quarta Coluna ----------------------------------------------------------------------------------------------------
btnC = Button(root,
                    text='C',
                    padx=31,
                    pady=20,
                    command=botaoApaga,
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#d95300',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=0, column=3)

btnSubtrai = Button(root,
                        text='-',
                        padx=30,
                        pady=20,
                        command=botaoSubtrai,
                        fg='#FFFFFF',
                        activeforeground='#d95300',
                        bg='#d95300',
                        activebackground='#FFFFFF',
                        font=('futura',12,'bold'),
                        relief=FLAT
                        ).grid(row=1, column=3)

btnSoma = Button(root,
                        text='+',
                        padx=30,
                        pady=20,
                        command=botaoSoma,
                        fg='#FFFFFF',
                        activeforeground='#d95300',
                        bg='#d95300',
                        activebackground='#FFFFFF',
                        font=('futura',12,'bold'),
                        relief=FLAT
                        ).grid(row=2, column=3)

btnIgual = Button(root,
                    text='=',
                    padx=30,
                    pady=57,
                    command=botaoIgual,
                    fg='#FFFFFF',
                    activeforeground='#d95300',
                    bg='#d95300',
                    activebackground='#FFFFFF',
                    font=('futura',12,'bold'),
                    relief=FLAT
                    ).grid(row=3, column=3, rowspan=2)



root.mainloop()