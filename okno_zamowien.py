from tkinter import *


def ekran_okna_zamowien(okno):
    global okno_zamowien
    okno_zamowien = Toplevel(okno)
    okno_zamowien.geometry('300x200')
    okno_zamowien.resizable(False, False)
    Button(okno_zamowien, text='Wroc', width=10, height=2, command=wroc).grid(column=0,row=0)
    Button(okno_zamowien, text='Nowe zamowienie',command=tworzenie_zamowienia).grid(column=1,row=0)


def wroc():
    okno_zamowien.destroy()


def tworzenie_zamowienia():
    from okno_tworzenia_zamowienia import ekran_tworzenia_zamowienia
    ekran_tworzenia_zamowienia(okno_zamowien)
