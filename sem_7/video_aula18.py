# Interfaces grafcas:
"""Para implementar programas com interfaces
gráficas (GUI) é necessário fazer uso de APIs
que fornecem funções para criação de
janelas, botões, gráficos e gerenciamento de
eventos."""

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='computer.gif').subsample(5)
imagem = Label(master=root, imagem=photo)
imagem.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Olá alunos da UNIVESP!')
text.pack(side=BOTTOM)
root.mainloop()

