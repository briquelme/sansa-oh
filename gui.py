import tkinter as tk
import cards
class window:

    def __init__(self,deck1,deck2,diccionario):
        '''n1,a1,d1 = deck1
        n2,a2,d2 = deck2'''
        self.j1 = cards.jugador(deck1[0], deck1[1], deck1[2])
        self.j2 = cards.jugador(deck2[0], deck2[1], deck2[2])
        '''self.j1 = j1
        self.j2 = j2'''

        print(type(self.j2))
        print(type(self.j2.card))
        print(type(self.j2.getDef()))


        self.diccionario = diccionario
        self.cv = tk.Canvas()
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
        self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')

        self.boton1 = tk.Button(self.cv, text="Atacar")#, command = self.ataque(self.j1, self.j2, self.diccionario))
        self.boton1.configure(width=10, activebackground="white")
        self.boton1_window = self.cv.create_window(420, 700, anchor=tk.NW, window=self.boton1)
        self.boton1.bind('<Button-1>', self.attackA)

        self.boton2 = tk.Button(self.cv, text="Sacrificar")#, command = self.sacrificar(self.j1,self.diccionario))
        self.boton2.configure(width=10, activebackground="white")
        self.boton2_window = self.cv.create_window(520, 700, anchor=tk.NW, window=self.boton2)

        self.boton3 = tk.Button(self.cv, text="Atacar")#, command = self.ataque(self.j2,self.j1,self.diccionario))
        self.boton3.configure(width=10, activebackground="white")
        self.boton3_window = self.cv.create_window(920, 700, anchor=tk.NW, window=self.boton3)
        self.boton3.bind('<Button-1>', self.attackB)

        self.boton4 = tk.Button(self.cv, text="Sacrificar")#, command = self.sacrificar(self.j2,self.diccionario))
        self.boton4.configure(width=10, activebackground="white")
        self.boton4_window =self.cv.create_window(1020, 700, anchor=tk.NW, window=self.boton4)

    def attackA(self, event):
        attack  = self.j1.getAtk()
        defense = self.j2.getDef()
        if attack > defense:
            self.j2.Hit()
            self.j2.ChangeCard(self.diccionario)
        elif attack < defense:
            self.j1.Hit()
            self.j1.ChangeCard(self.diccionario)
        else:
            self.j1.ChangeCard(self.diccionario)
            self.j2.ChangeCard(self.diccionario)
        self.cv.update()

    def attackB(self, event):
        attack  = self.j2.getAtk()
        defense = self.j1.getDef()
        if attack > defense:
            self.j1.Hit()
            self.j1.ChangeCard(self.diccionario)
        elif attack < defense:
            self.j2.Hit()
            self.j2.ChangeCard(self.diccionario)
        else:
            self.j1.ChangeCard(self.diccionario)
            self.j2.ChangeCard(self.diccionario)
        self.cv.update()

    def tributeA(self, event):
        self.j1.UseTribute(self.diccionario)
        self.cv.update()

    def tributeB(self, event):
        self.j2.UseTribute(self.diccionario)
        self.cv.update()