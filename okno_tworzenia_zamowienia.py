from tkinter import *
import sqlite3
import os


def ekran_tworzenia_zamowienia(okno):
    global okno_tworzenia_zamowien
    okno_tworzenia_zamowien=Toplevel(okno)
    okno_tworzenia_zamowien.geometry('700x400')
    okno_tworzenia_zamowien.title('Formularz przyjecia')
    # obramowania
    Frame(okno_tworzenia_zamowien, width=350, height=400, bd=8, relief='raise').place(x=0, y=0)
    Frame(okno_tworzenia_zamowien, width=350, height=200, bd=8, relief='raise').place(x=350, y=0)
    Frame(okno_tworzenia_zamowien, width=350, height=200, bd=8, relief='raise').place(x=350, y=200)
    # potrzebne do bazy danych
    global nazwisko
    global telefon
    global vin
    global marka
    global model
    global nr_rej
    global opis
    nazwisko = StringVar()
    telefon = IntVar()
    vin = StringVar()
    marka = StringVar()
    model = StringVar
    nr_rej = StringVar()
    opis = StringVar()
    # GUI
    Label(okno_tworzenia_zamowien, text='Nazwisko', font =('Arial',11)).place(x=15, y=10)
    pole_nazwiska = Entry(okno_tworzenia_zamowien, textvariable=nazwisko)
    pole_nazwiska.place(x=90, y=14)
