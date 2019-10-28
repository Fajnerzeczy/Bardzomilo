from tkinter import *
import sqlite3


def ekran_tworzenia_zamowienia(okno):
    global okno_tworzenia_zamowien
    okno_tworzenia_zamowien = Toplevel(okno)
    okno_tworzenia_zamowien.resizable(False, False)
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
    telefon = StringVar()
    vin = StringVar()
    marka = StringVar()
    model = StringVar()
    nr_rej = StringVar()
    opis = StringVar()
    # GUI
    Label(okno_tworzenia_zamowien, text='Nazwisko', font=('Arial', 11)).place(x=15, y=10)
    pole_nazwiska = Entry(okno_tworzenia_zamowien, textvariable=nazwisko)
    pole_nazwiska.place(x=90, y=14)
    Label(okno_tworzenia_zamowien, text='Nr telefonu', font=('Arial', 11)).place(x=13, y=40)
    pole_telefon = Entry(okno_tworzenia_zamowien, textvariable=telefon)
    telefon.trace('w', lambda *args: limit_znakow_telefon(telefon))
    pole_telefon.place(x=90, y=44)
    Label(okno_tworzenia_zamowien, text='Nr VIN', font=('Arial', 11)).place(x=15, y=70)
    pole_vin = Entry(okno_tworzenia_zamowien, textvariable=vin)
    vin.trace('w', lambda *args: limit_znakow_vin(vin))
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
    Label(okno_tworzenia_zamowien, text='Krotki opis (50 znakow)', font=('Arial', 11)).place(x=360, y=10)
    pole_opisu = Entry(okno_tworzenia_zamowien, width=50, textvariable=opis)
    opis.trace('w', lambda *args: limit_znakow_opis(opis))
    pole_opisu.place(x=360, y=40)
    Button(okno_tworzenia_zamowien, text='Dodaj', command=dodaj_do_bazy).place(x=640, y=360)
    Button(okno_tworzenia_zamowien, text='Anuluj', command=wroc).place(x=560, y=360)


# Usunwanie okien
def wroc():
    global okno_anulowania
    okno_anulowania = Toplevel(okno_tworzenia_zamowien)
    okno_anulowania.geometry('200x60')
    okno_anulowania.resizable(False, False)
    Label(okno_anulowania, text='Czy chcesz anulowac zamowienie?').pack()
    Button(okno_anulowania, text='Tak', command=usun_wroc_tak).place(x=50, y=30)
    Button(okno_anulowania, text='Nie', command= usun_wroc_nie).place(x=120, y=30)


def usun_wroc_tak():
    okno_anulowania.destroy()
    okno_tworzenia_zamowien.destroy()


def usun_wroc_nie():
    okno_anulowania.destroy()


def usun_pomyslnie_dodano():
    okno_dodania.destroy()
    okno_tworzenia_zamowien.destroy()


# Limity znakow
def limit_znakow_vin(pole):
    if len(pole.get()) > 0:
        pole.set(pole.get()[:17])


def limit_znakow_telefon(pole):
    if len(pole.get()) > 0:
        pole.set(pole.get()[:9])


def limit_znakow_opis(pole):
    if len(pole.get()) > 0:
        pole.set(pole.get()[:50])

# Laczenie z baza
def dodaj_do_bazy():
    nazwisko1 = nazwisko.get()
    telefon1 = telefon.get()
    vin1 = vin.get()
    marka1 = marka.get()
    model1 = model.get()
    nr_rej1 = nr_rej.get()
    opis1 = opis.get()
    polacz = sqlite3.connect('baza.db')
    with polacz:
        kursor = polacz.cursor()
        kursor.execute('INSERT INTO Zamowienia(Nazwisko,Telefon,Vin,Marka,Model,Nr_rej,Opis) VALUES(?,?,?,?,?,?,?)',
                       (nazwisko1, telefon1, vin1, marka1, model1, nr_rej1,opis1))
        kursor.close()
    # Popout
    global okno_dodania
    okno_dodania = Toplevel(okno_tworzenia_zamowien)
    okno_dodania.geometry('200x70')
    okno_dodania.resizable(False, False)
    Label(okno_dodania, text='Pomyslnie dodano zamowienie\n').pack()
    Button(okno_dodania, text='OK', command=usun_pomyslnie_dodano).pack()
