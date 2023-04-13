"""Script que recibe configuración inicial y prepara objetos necesarios para
iniciar el juego.
"""
import cards
import gui
import sys
import tkinter as tk

"""Loop para configurar cantidad de vidas. Se checkea la validez del input a
través de exceptions
"""
while True:
    try:
        lives = int(input("Ingrese cantidad de vidas: \n"))
        if lives <= 0:
            raise Exception()
        break
    except (ValueError,Exception):
        print("Ingrese un numero valido")

"""Loop para configurar quien empieza. Se checkea la validez del input a
través de exceptions
"""
while True:
    try:
        turno = input("Quien parte? (Ingrese j1 o j2): ")
        if turno != "j1" and turno != "j2":
            raise Exception
        break
    except Exception:
        print("Ingrese un string valido")

"""Carga de mazo y elección de cartas iniciales."""
mazo,cant = cards.cardgen()
tupla1 = cards.cardchooser(mazo)
tupla2 = cards.cardchooser(mazo)

"""Construcción de ventana y tamaño a ventana completa dependiendo de
plataforma empleada.
"""
root = tk.Tk()
root.title("Sansa-Oh")
platform = sys.platform
# Caso linux
if platform == 'linux':
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()        
    root.geometry("%dx%d+0+0"%(w,h))
# Caso windows
elif platform == 'win32':
    root.wm_state('zoomed')

"""Entrega de parámetros para construcción de canvas e inicio del juego"""
test = gui.window(tupla1,tupla2, mazo,turno,lives)
root.mainloop()
