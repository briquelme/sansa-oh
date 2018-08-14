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

lives = int(input("Ingrese cantidad de vidas: "))

test = gui.window(tupla1,tupla2, mazo,lives)
root.mainloop()
