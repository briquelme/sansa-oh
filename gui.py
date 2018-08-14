import tkinter as tk
import cards
class window:

    def __init__(self,deck1,deck2,diccionario,turno, vidas = 3):
        self.j1 = cards.jugador(deck1[0], deck1[1], deck1[2],vidas)
        self.j2 = cards.jugador(deck2[0], deck2[1], deck2[2],vidas)
        self.turno = turno
        self.diccionario = diccionario
        self.cv = tk.Canvas()
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
        self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')

        self.textVictoria = tk.StringVar()
        self.textVictoria.set("No hay Ganador aun")
        self.VictoriaDisplay = tk.Label(self.cv,textvariable = self.textVictoria)
        self.VictoriaDisplay.place(x = 5, y = 300, anchor = tk.NW)

        self.textTurno = tk.StringVar()
        self.textTurno.set(self.turno)

        self.TurnoHead = tk.Label(self.cv,text = "Turno Actual: ")
        self.TurnoHead.place(x= 700, y= 650, anchor = tk.NW)
        self.TurnoDisplay = tk.Label(self.cv, textvariable = self.textTurno)
        self.TurnoDisplay.place(x = 780, y= 650, anchor = tk.NW)

        self.textHP1 = tk.StringVar()
        self.textHP2 = tk.StringVar()#Para pasar vidas de los jugadores a tkinter

        self.textHP1.set(str(self.j1.vida))
        self.textHP2.set(str(self.j2.vida))#inicializar vidas para tkinter

        self.HP1Head = tk.Label(self.cv, text = 'Vidas: ')
        self.HP1Head.place(x = 420, y= 740, anchor = tk.NW)
        self.HP2Head = tk.Label(self.cv, text = 'Vidas: ')
        self.HP2Head.place(x = 920, y= 740, anchor = tk.NW)#titulos para vida
        
        self.HP1Display = tk.Label(self.cv, textvariable = self.textHP1)
        self.HP1Display.place (x = 520, y = 740, anchor = tk.NW)
        self.HP2Display = tk.Label(self.cv, textvariable = self.textHP2)
        self.HP2Display.place (x = 1020, y = 740, anchor = tk.NW)#display dinamicos para vidas

        self.textTrib1 = tk.StringVar()
        self.textTrib2 = tk.StringVar()#variables para pasar sacrificios a tkinter

        self.textTrib1.set(str(self.j1.sacrificios))
        self.textTrib2.set(str(self.j2.sacrificios))#inicializar sacrificios tkinter

        self.Trib1Head = tk.Label(self.cv, text = 'Sacrificios: ')
        self.Trib1Head.place(x = 420, y= 761, anchor = tk.NW)
        self.Trib2Head = tk.Label(self.cv, text = 'Sacrificios: ')
        self.Trib2Head.place(x = 920, y= 761, anchor = tk.NW)#titulos para sacrificios

        self.Trib1Display = tk.Label(self.cv, textvariable = self.textTrib1)
        self.Trib1Display.place (x = 520, y = 761, anchor = tk.NW)
        self.Trib2Display = tk.Label(self.cv, textvariable = self.textTrib2)
        self.Trib2Display.place (x = 1020, y = 761, anchor = tk.NW)#display dinamicos para sacrificios

        self.boton1 = tk.Button(self.cv, text="Atacar")#, command = self.ataque(self.j1, self.j2, self.diccionario))
        self.boton1.configure(width=10, activebackground="white")
        self.boton1_window = self.cv.create_window(420, 700, anchor=tk.NW, window=self.boton1)
        self.boton1.bind('<Button-1>', self.attackA)

        self.boton2 = tk.Button(self.cv, text="Sacrificar")#, command = self.sacrificar(self.j1,self.diccionario))
        self.boton2.configure(width=10, activebackground="white")
        self.boton2_window = self.cv.create_window(520, 700, anchor=tk.NW, window=self.boton2)
        self.boton2.bind('<Button-1>', self.tributeA)

        self.boton3 = tk.Button(self.cv, text="Atacar")#, command = self.ataque(self.j2,self.j1,self.diccionario))
        self.boton3.configure(width=10, activebackground="white")
        self.boton3_window = self.cv.create_window(920, 700, anchor=tk.NW, window=self.boton3)
        self.boton3.bind('<Button-1>', self.attackB)

        self.boton4 = tk.Button(self.cv, text="Sacrificar")#, command = self.sacrificar(self.j2,self.diccionario))
        self.boton4.configure(width=10, activebackground="white")
        self.boton4_window =self.cv.create_window(1020, 700, anchor=tk.NW, window=self.boton4)
        self.boton4.bind('<Button-1>', self.tributeB)

    def attackA(self, event):
        if self.turno == "j1":
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
            self.textHP1.set(str(self.j1.vida))
            self.textHP2.set(str(self.j2.vida))
        #Enzi
            self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
            self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')
            self.turno = "j2"
            self.checkear()
            self.textTurno.set(self.turno)
            self.cv.update()

    def attackB(self, event):
        if self.turno == "j2":
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
            self.textHP1.set(str(self.j1.vida))
            self.textHP2.set(str(self.j2.vida))
        #Enzi
            self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
            self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')
            self.turno = "j1"
            self.checkear()
            self.textTurno.set(self.turno)
            self.cv.update()

    def tributeA(self, event):
        if self.turno == "j1":
            self.j1.UseTribute(self.diccionario)
            self.textTrib1.set(str(self.j1.sacrificios))
        #Enzi
            self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
            self.turno = "j2"
            self.textTurno.set(self.turno)
            self.cv.update()

    def tributeB(self, event):
        if self.turno == "j2":
            self.j2.UseTribute(self.diccionario)
            self.textTrib2.set(str(self.j2.sacrificios))
        #Enzi
            self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')
            self.turno = "j1"
            self.textTurno.set(self.turno)
            self.cv.update()

    def checkear(self):
        if self.j1.getVida() == 0:
            self.textVictoria.set("Jugador 2 ha Ganado \n puede salir del juego")
            self.turno = "Fin Partida"
            self.cv.update()
        elif self.j2.getVida() == 0:
            self.textVictoria.set("Jugador 1 ha Ganado \npuede salir del juego")
            self.turno = "Fin Partida"
            self.cv.update()


