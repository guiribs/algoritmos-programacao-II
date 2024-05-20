# Programação Orientada a Eventos

# Primeiro exemplo: janela com um botão que, quando clicado, exibe o dia e a hora na tela. 

from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S%p\n', localtime())
    showinfo(message=time)
    
root = Tk()
button = Button(root, text="Clique", command=clicked)
button.pack()
root.mainloop()

# Segundo exemplo: caixa de inserção de texto.

from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

def compute():
        global entry
        date = entry.get()
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))
        showinfo(message='{} was a {}'.format(date, weekday))

root = Tk()
label = Label(root, text='Digite uma data: ')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()

# Terceiro exemplo: caixa de texto com diferentes eventos.

from tkinter import Tk, Text, BOTH

def key_pressed(event):
    print('char: {}'.format(event.keysym))
def mouse_clicked_left(event):
    print('mouse left clicked')
def mouse_clicked_right(event):
    print('mouse right clicked')
    
root = Tk()
text = Text(root, width=20, height='5')
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_clicked_left)
text.bind('<Button-2>', mouse_clicked_right)
text.pack(expand=True, fill=BOTH)
root.mainloop()