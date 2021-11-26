import tkinter as tk
okno=tk.Tk()
okno.title("Imię")
tekst=tk.StringVar()
label=tk.Label( okno, textvariable = tekst).pack()
tekst.set("witaj przyjacielu")
imie=tk.Label(text="podaj imię").pack()
wpisz=tk.Entry()
wpisz.pack()
def wyswietl():
    tekst.set("witaj {0} przyjacielu".format(wpisz.get()))
guzik=tk.Button(text="okej", command=wyswietl)
guzik.pack()
tk.mainloop() 