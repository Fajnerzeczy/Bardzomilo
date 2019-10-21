from tkinter import *


def ekran_menu_glownego(nazwa):
    global menu_glowne
    menu_glowne = Tk()
    menu_glowne.geometry('500x220')
    menu_glowne.title('Menu')
    menu_glowne.configure(background='black')
    menu_glowne.grid_rowconfigure(0, weight=1)
    menu_glowne.grid_columnconfigure(0, weight=1)
    Frame(menu_glowne, width=500, height=100, bd=8, relief='raise').grid(row=0, column=0, columnspan=4)
    Frame(menu_glowne, width=500, height=120, bd=8, relief='raise').grid(row=1, column=0, columnspan=4, rowspan=2)
    Label(menu_glowne, text=f'Witaj, {nazwa}', font=('Arial', 20, 'bold')).place(x=180, y=25)
    Button(menu_glowne, text='Zarzadzaj zamowieniami', height=2, width=20, command=zamowienia).place(x=180, y=110)
    Button(menu_glowne, text='Harmonogram', height=2, width=20).place(x=180, y=150)
    Button(menu_glowne, text='Wyloguj', height=2, width=10, command=wyloguj).place(x=400, y=25)
    Button(menu_glowne, text='Ustawienia konta', height=2, width=15).place(x=20, y=150)
    menu_glowne.mainloop()


def wyloguj():
    menu_glowne.destroy()
    from okno_logowania import ekran_okna_glownego
    ekran_okna_glownego()


def zamowienia():
    from okno_zamowien import ekran_okna_zamowien
    ekran_okna_zamowien(menu_glowne)
