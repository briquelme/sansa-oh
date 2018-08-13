import cards
import gui
import tkinter as tk
mazo,cant = cards.cardgen()
root = tk.Tk()
root.title("Sansa-Oh")
'''n1,a1,d1 = mazo[1]
n2,a2,d2 = mazo[2]
ju1 = cards.jugador(n1,a1,d1)
ju2 = cards.jugador(n2,a2,d2)'''


test = gui.window(mazo[1], mazo[2], mazo)
root.mainloop()
