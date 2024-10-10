from tkinter import *
from tkinter.messagebox import showerror


#Creating function of add_text
def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')

def submit(entry:Entry, strvar:StringVar):
    operation=entry.get()
    try:
        strvar.set(f"{strvar.get()}={eval(operation)}")
    except:
        showerror('Error!','Please enter a properly defined equation!')



#Creating the GUI
screen=Tk()
screen.title("Numeric Calculator")
screen.geometry('260x500')
screen.resizable(0,0)
screen.configure(background='Burlywood')

entry_strvar = StringVar(screen)

Label(screen, text='Numeric',    font=("Comic Sans MS", 20), bg='Burlywood').place(x=25, y=0)
Label(screen, text='**CALCULATOR**', font=("Comic Sans MS", 15), bg='Burlywood').place(x=30, y=35)

eqn_entry = Entry(screen, justify=RIGHT, textvariable=entry_strvar, width=19, font=25, state='disabled').place(x=10, y=70)

# Number Buttons
Button(screen, height=2, width=5, text='7', font=9, bg='Beige', command=lambda: add_text("7", entry_strvar)).place(x=5, y=170)
Button(screen, height=2, width=5, text='8', font=9, bg='Beige', command=lambda: add_text('8', entry_strvar)).place(x=65, y=170)
Button(screen, height=2, width=5, text='9', font=9, bg='Beige', command=lambda: add_text('9', entry_strvar)).place(x=125, y=170)
Button(screen, height=2, width=5, text='4', font=9, bg='Beige', command=lambda: add_text('4', entry_strvar)).place(x=5, y=225)
Button(screen, height=2, width=5, text='5', font=9, bg='Beige', command=lambda: add_text('5', entry_strvar)).place(x=65, y=225)
Button(screen, height=2, width=5, text='6', font=9, bg='Beige', command=lambda: add_text('6', entry_strvar)).place(x=125, y=225)
Button(screen, height=2, width=5, text='1', font=9, bg='Beige', command=lambda: add_text('1', entry_strvar)).place(x=5, y=280)
Button(screen, height=2, width=5, text='2', font=9, bg='Beige', command=lambda: add_text('2', entry_strvar)).place(x=65, y=280)
Button(screen, height=2, width=5, text='3', font=9, bg='Beige', command=lambda: add_text('3', entry_strvar)).place(x=125, y=280)
Button(screen, height=2, width=5, text='0', font=9, bg='Beige', command=lambda: add_text('0', entry_strvar)).place(x=5, y=340)

# Operator Buttons
add          = Button(screen, height=2, width=5, text='+', font=9, bg='GOld', command=lambda: add_text('+', entry_strvar)).place(x=195, y=340)
subtract     = Button(screen, height=2, width=5, text='-', font=9, bg='GOld', command=lambda: add_text('-', entry_strvar)).place(x=195, y=280)
multiply     = Button(screen, height=2, width=5, text='x', font=9, bg='GOld', command=lambda: add_text('*', entry_strvar)).place(x=195, y=225)
divide       = Button(screen, height=2, width=5, text='/', font=9, bg='GOld', command=lambda: add_text('/', entry_strvar)).place(x=195, y=170)
modulus      = Button(screen, height=2, width=5, text='%', font=9, bg='GOld', command=lambda: add_text('%', entry_strvar)).place(x=195, y=110)
decimal      = Button(screen, height=2, width=5, text='.', font=9, bg='Khaki', command=lambda: add_text('.', entry_strvar)).place(x=65, y=340)
bracket_open = Button(screen, height=2, width=5, text='(', font=9, bg='GOld', command=lambda: add_text('.', entry_strvar)).place(x=65, y=110)
bracket_close= Button(screen, height=2, width=5, text=')', font=9, bg='GOld', command=lambda: add_text('.', entry_strvar)).place(x=125, y=110)

# Equal, C and AC buttons
equal = Button(screen, height=2, width=5, text='=', font=9, bg='ForestGreen', command=lambda: submit(eqn_entry, entry_strvar)).place(x=125, y=340)
clear = Button(screen, height=1, width=5, text='C', font=9, bg='Red', command=lambda: entry_strvar.set(entry_strvar.get()[:-1])).place(x=195, y=65)
AC_btn= Button(screen, height=2, width=5, text='AC', font=9, bg='Brown', command=lambda: entry_strvar.set('')).place(x=5, y=110)

# Ok Button
ok_btn = Button(screen, height=2, width=22, text='Ok', font=9, bg='CadetBlue', command=lambda: screen.destroy())
ok_btn.place(x=20, y=420)

# Updating screen
screen.update()
screen.mainloop()