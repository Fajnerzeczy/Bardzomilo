from tkinter import *
import sqlite3
import os


def ekran_tworzenia_zamowienia(okno):
    global okno_tworzenia_zamowien
    okno_tworzenia_zamowien = Toplevel(okno)
    okno_tworzenia_zamowien.resizable(width=False, height=False)
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
    Label(okno_tworzenia_zamowien, text='Nazwisko', font=('Arial', 11)).place(x=15, y=10)
    pole_nazwiska = Entry(okno_tworzenia_zamowien, textvariable=nazwisko)
    pole_nazwiska.place(x=90, y=14)
    Label(okno_tworzenia_zamowien, text='Nr telefonu', font=('Arial', 11)).place(x=13, y=40)
    pole_telefon = Entry(okno_tworzenia_zamowien, textvariable=telefon)
    pole_telefon.place(x=90, y=44)
    Label(okno_tworzenia_zamowien, text='Nr VIN', font=('Arial', 11)).place(x=15, y=70)
    pole_vin = Entry(okno_tworzenia_zamowien, textvariable=vin)
    pole_vin.place(x=90, y=74)
    Label(okno_tworzenia_zamowien, text='Marka', font=('Arial', 11)).place(x=15, y=100)
    pole_marki = Entry(okno_tworzenia_zamowien, textvariable=marka)
    pole_marki.place(x=90, y=104)
    Label(okno_tworzenia_zamowien, text='Model', font=('Arial', 11)).place(x=15, y=130)
    pole_modelu = Entry(okno_tworzenia_zamowien, textvariable=model)
    pole_modelu.place(x=90, y=134)
    Label(okno_tworzenia_zamowien, text='Rejestracja', font=('Arial', 11)).place(x=12, y=160)
    pole_nr_rej = Entry(okno_tworzenia_zamowien, textvariable=nr_rej)
    pole_nr_rej.place(x=90, y=164)
    Label(okno_tworzenia_zamowien, text='Opis', font=('Arial', 11)).place(x=360, y=10)
    pole_opisu = Text(okno_tworzenia_zamowien, width=40, height=7, font=('Arial', 11))  # to jest jakies zjebane
    pole_opisu.place(x=360, y=40)
