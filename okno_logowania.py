from tkinter import *
import os
from okno_glowne import *


def ekran_okna_glownego():
    global okno_glowne
    okno_glowne = Tk()
    okno_glowne.geometry('250x150')
    okno_glowne.title('Cos')
    Label(okno_glowne, text='Nasza apka\n', font=('Arial', 15)).pack()
    Button(okno_glowne, text='Zaloguj sie', height='2', width='10', command=ekran_okna_logowania).pack()
    okno_glowne.mainloop()


def ekran_okna_logowania():
    global okno_logowania
    global pole_login
    global pole_hasla
    global weryfikacja_loginu
    global weryfikacja_hasla

    weryfikacja_loginu = StringVar()
    weryfikacja_hasla = StringVar()
    okno_logowania = Toplevel(okno_glowne)
    okno_logowania.title('Zaloguj sie')
    okno_logowania.geometry('250x150')
    Label(okno_logowania, text='Login').pack()
    pole_login = Entry(okno_logowania, textvariable=weryfikacja_loginu)
    pole_login.pack()
    Label(okno_logowania, text='Haslo').pack()
    pole_hasla = Entry(okno_logowania, textvariable=weryfikacja_hasla, show='*')
    pole_hasla.pack()
    Button(okno_logowania, text='Zaloguj', width=15, height=2, command=sprawdzanie_logowania).pack()


def sprawdzanie_logowania():
    login1 = weryfikacja_loginu.get()
    haslo1 = weryfikacja_hasla.get()
    pole_hasla.delete(0, END)
    plik = os.listdir()
    if login1 in plik:
        plik1 = open(login1, "r")
        sprawdz = plik1.read().splitlines()
        if haslo1 in sprawdz:
            ekran_pomyslnego_zalogowania()
        else:
            ekran_zlego_hasla()
    else:
        ekran_braku_uzytkownika()


def ekran_pomyslnego_zalogowania():
    global okno_pomyslnego_zalogowania
    okno_pomyslnego_zalogowania = Toplevel(okno_logowania)
    okno_pomyslnego_zalogowania.title('Pomyslnie zalogowano')
    okno_pomyslnego_zalogowania.geometry('150x100')
    Label(okno_pomyslnego_zalogowania, text='Pomyslnie zalogowano').pack()
    Button(okno_pomyslnego_zalogowania, text='Dalej', command=usun_ekran_pomyslnego_logowania).pack()


def ekran_zlego_hasla():
    global okno_zlego_hasla
    okno_zlego_hasla = Toplevel(okno_logowania)
    okno_zlego_hasla.title('Zle haslo')
    okno_zlego_hasla.geometry('100x100')
    Label(okno_zlego_hasla, text='Zle haslo').pack()
    Button(okno_zlego_hasla, text='Wroc', command=usun_ekran_zlego_hasla).pack()


def ekran_braku_uzytkownika():
    global okno_braku_uzytkownika
    okno_braku_uzytkownika = Toplevel(okno_logowania)
    okno_braku_uzytkownika.title('Nie znaleziono uzytkownika')
    okno_braku_uzytkownika.geometry('150x100')
    Label(okno_braku_uzytkownika, text='Nie znaleziono uzytkownika').pack()
    Button(okno_braku_uzytkownika, text='Wroc', command=usun_ekran_braku_uzytkownika).pack()


# do usuwania
def usun_ekran_pomyslnego_logowania():
    okno_pomyslnego_zalogowania.destroy()
    okno_logowania.destroy()
    okno_glowne.destroy()
    ekran_menu_glownego(weryfikacja_loginu.get())


def usun_ekran_zlego_hasla():
    okno_zlego_hasla.destroy()


def usun_ekran_braku_uzytkownika():
    okno_braku_uzytkownika.destroy()


ekran_okna_glownego()
