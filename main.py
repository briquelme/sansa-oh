import cards
import gui
import tkinter as tk
mazo,cant = cards.cardgen()
root = tk.Tk()
root.title("Sansa-Oh")
#root.attributes('-fullscreen', True)
root.wm_state('zoomed')
tupla1 = cards.cardchooser(mazo)
tupla2 = cards.cardchooser(mazo)
while True:
    try:
        lives = int(input("Ingrese cantidad de vidas: \n"))
        if lives <= 0:
            raise Exception()
        break
    except (ValueError,Exception):
        print("Ingrese un numero valido")
while True:
    try:
        turno = input("Quien parte? (Ingrese j1 o j2): ")
        if turno != "j1" and turno != "j2":
            raise Exception
        break
    except Exception:
        print("Ingrese un string valido")

test = gui.window(tupla1,tupla2, mazo,turno,lives)
root.mainloop()
