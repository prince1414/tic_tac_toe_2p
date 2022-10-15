from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title('TIC-TAC-TOE~XO')

#Framework
def disable_all():
    b1.config(state = 'disable')
    b2.config(state='disable')
    b3.config(state='disable')

    b4.config(state='disable')
    b5.config(state='disable')
    b6.config(state='disable')

    b7.config(state='disable')
    b8.config(state='disable')
    b9.config(state='disable')

def check_win():
    global winner = False
    winner = False
    win = 'light green'

    # X
    if b1['text'] + b2['text'] + b3['text'] == 'XXX':
        b1.config(bg= win )
        b2.config(bg= win )
        b3.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    elif b4['text'] + b5['text'] + b6['text'] == 'XXX':
        b4.config(bg= win )
        b5.config(bg= win )
        b6.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    elif b7['text'] + b8['text'] + b9['text'] == 'XXX':
        b7.config(bg= win )
        b8.config(bg= win )
        b9.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    elif b1['text'] + b4['text'] + b7['text'] == 'XXX':
        b1.config(bg= win )
        b4.config(bg= win )
        b7.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    elif b2['text'] + b5['text'] + b8['text'] == 'XXX':
        b2.config(bg= win )
        b5.config(bg= win )
        b8.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    elif b3['text'] + b6['text'] + b9['text'] == 'XXX':
        b3.config(bg= win )
        b6.config(bg= win )
        b9.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    elif b1['text'] + b5['text'] + b9['text'] == 'XXX':
        b1.config(bg= win )
        b5.config(bg= win )
        b9.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    elif b3['text'] + b5['text'] + b7['text'] == 'XXX':
        b3.config(bg= win )
        b5.config(bg= win )
        b7.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'X wins')
        disable_all()

    #O

    elif b1['text'] + b2['text'] + b3['text'] == 'OOO':
        b1.config(bg= win )
        b2.config(bg= win )
        b3.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()

    elif b4['text'] + b5['text'] + b6['text'] == 'OOO':
        b4.config(bg= win )
        b5.config(bg= win )
        b6.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()

    elif b7['text'] + b8['text'] + b9['text'] == 'OOO':
        b7.config(bg= win )
        b8.config(bg= win )
        b9.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()

    elif b1['text'] + b4['text'] + b7['text'] == 'OOO':
        b1.config(bg= win )
        b4.config(bg= win )
        b7.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()

    elif b2['text'] + b5['text'] + b8['text'] == 'OOO':
        b2.config(bg= win )
        b5.config(bg= win )
        b8.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()

    elif b3['text'] + b6['text'] + b9['text'] == 'OOO':
        b3.config(bg= win )
        b6.config(bg= win )
        b9.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()

    elif b1['text'] + b5['text'] + b9['text'] == 'OOO':
        b1.config(bg= win )
        b5.config(bg= win )
        b9.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()

    elif b3['text'] + b5['text'] + b7['text'] == 'OOO':
        b3.config(bg= win )
        b5.config(bg= win )
        b7.config(bg= win )
        winner = True
        messagebox.showinfo('TIC-TAC-TOE', 'O wins')
        disable_all()
    elif count == 9 and winner == False:
        messagebox.showinfo('TIC-TAC-TOE', 'Tie, No one wins.')
        b1.config(bg='light yellow')
        b2.config(bg='light yellow')
        b3.config(bg='light yellow')
        b4.config(bg='light yellow')
        b5.config(bg='light yellow')
        b6.config(bg='light yellow')
        b7.config(bg='light yellow')
        b8.config(bg='light yellow')
        b9.config(bg='light yellow')
        disable_all()

def b_click(b):
    global count,clicked
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        check_win()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        check_win()
    else:
        messagebox.showerror('TIC-TAC-TOE','Already Filled')

def reset_f():
    global count, clicked
    count = 0
    clicked = True

    global b1,b2,b3,b4,b5,b6,b7,b8,b9

    #Creating buttons

    #1st row
    b1 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b1))
    b2 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b2))
    b3 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b3))
    #2nd row
    b4 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b4))
    b5 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b5))
    b6 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b6))
    #3rd row
    b7 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b7))
    b8 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b8))
    b9 = Button(screen, text = ' ', font = ('COMIC SANS MS',20),height = 3, width = 6,bg = 'white', command = lambda : b_click(b9))


    #Positions



    #1st row
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    #2nd row
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    #3rd row
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)


#reset button

reset_b = Button(screen, text = 'RESET', font = ('TIMES NEW ROMAN',15),bg = 'white', command = lambda : reset_f())
reset_b.grid(row = 3 , column = 1 )
reset_f()
