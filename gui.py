"""Construcción de canvas para interfáz gráfica y almacenamiento
de clases y métodos asociados a lógica del juego.
"""
import tkinter as tk
import cards
class window:
    """Clase que almacena los objetos del juego y el canvas, además de gestionar
    la lógica del juego.

    Attributes:
        j1 (cards.jugador): instancia que representa al jugador 1
        j2 (cards.jugador): instancia que representa al jugador 2
        turno (str): indica si inicia el jugador 1 ('j1') o jugador 2 ('j2')
        diccionario ({int:[str,int,int]}): Diccionario compatible al generado 
            por función 'cardgen'. Representa mazo de cartas disponibles.
        cv (tkinter.Canvas): canvas de la interfaz.
        textVictoria (tkinter.StringVar) : texto indicando al ganador.
        VictoriaDisplay (tkinter.Label) : Objeto que dibuja a 'textVictoria' 
            en el canvas.    
        textTurno (tkinter.StringVar) : texto indicando de quien es el turno
            actual.
        TurnoDisplay (tkinter.Label) : Objeto que dibuja a 'textTurno' en el 
            canvas.
        TurnoHead(tkinter.Label) : Header del indicador de turno actual.
        textHP1 (tkinter.StringVar) : texto indicando vida actual del 
            jugador 1.
        HP1Display (tkinter.Label) : Objeto que dibuja a 'textHP1' en el 
            canvas.
        HP1Head(tkinter.Label) : Header del indicador de vida jugador 1.
        textHP2 (tkinter.StringVar) : texto indicando vida actual del 
            jugador 2.
        HP2Display (tkinter.Label) : Objeto que dibuja a 'textHP2' en el 
            canvas.
        HP2Head(tkinter.Label) : Header del indicador de vida jugador 2.
        textTrib1 (tkinter.StringVar) : texto indicando sacrificios disponibles 
            del jugador 1.
        Trib1Display (tkinter.Label) : Objeto que dibuja a 'textTrib1' en el 
            canvas.
        Trib1Head(tkinter.Label) : Header del indicador de sacrificios jugador 
            1.
        textTrib2 (tkinter.StringVar) : texto indicando sacrificios disponibles
            del jugador 2.
        Trib2Display (tkinter.Label) : Objeto que dibuja a 'textTrib2' en el 
            canvas.
        Trib2Head(tkinter.Label) : Header del indicador de sacrificios jugador 
            2.
        botonX (tkinter.Button) : botones dispuestos en la interfaz. El número
            'X' indica el significado del boton:
                1: Ataque del jugador 1.
                2: Sacrificio del jugador 1.
                3: Ataque del jugador 2.
                4: Sacrificio del jugador 2.
    """
    def __init__(self,deck1,deck2,diccionario,turno, vidas = 3):
        # Inicializar objetos del juego con parámetros entregados.
        self.j1 = cards.jugador(deck1[0], deck1[1], deck1[2],vidas)
        self.j2 = cards.jugador(deck2[0], deck2[1], deck2[2],vidas)
        self.turno = turno
        self.diccionario = diccionario
        
        # Construcción canvas y construcción de elementos UI
        self.cv = tk.Canvas()
        self.cv.pack(side='top', fill='both', expand='yes')

        # Carga imágenes cartas
        self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
        self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')

        """Indicador de ganador. tkinter.StringVar permite almacenar y 
        actualizar un str que será presentado en UI. Es presentado
        a través del parámetro 'textvariable' del constructor de
        tkinter.Label"""
        self.textVictoria = tk.StringVar()
        self.textVictoria.set("No hay Ganador aun")
        self.VictoriaDisplay = tk.Label(self.cv,textvariable = self.textVictoria)
        self.VictoriaDisplay.place(x = 5, y = 300, anchor = tk.NW)

        """Indicador de turno actual, indicando "j1" o "j2" Ejemplo en pantalla:
          * 'Turno Actual: j1'"""
        self.textTurno = tk.StringVar()
        self.textTurno.set(self.turno)
        # Entregar StringVar a Label
        self.TurnoDisplay = tk.Label(self.cv, textvariable = self.textTurno)
        self.TurnoDisplay.place(x = 780, y= 650, anchor = tk.NW)
        # El indicador presenta un header. Al ser un str invariable, se usa el
        # parámetro 'text' en estos casos.
        self.TurnoHead = tk.Label(self.cv,text = "Turno Actual: ")
        self.TurnoHead.place(x= 700, y= 650, anchor = tk.NW)

        """Indicadores para vida. Sigue misma lógica del indicador de turno.
        Ejemplo en pantalla:
          * 'Vidas:        10'"""
        self.textHP1 = tk.StringVar()
        self.textHP2 = tk.StringVar()
        self.textHP1.set(str(self.j1.vida))
        self.textHP2.set(str(self.j2.vida))
        self.HP1Display = tk.Label(self.cv, textvariable = self.textHP1)
        self.HP1Display.place (x = 520, y = 740, anchor = tk.NW)
        self.HP2Display = tk.Label(self.cv, textvariable = self.textHP2)
        self.HP2Display.place (x = 1020, y = 740, anchor = tk.NW)
        self.HP1Head = tk.Label(self.cv, text = 'Vidas: ')
        self.HP1Head.place(x = 420, y= 740, anchor = tk.NW)
        self.HP2Head = tk.Label(self.cv, text = 'Vidas: ')
        self.HP2Head.place(x = 920, y= 740, anchor = tk.NW)
        
        """Indicadores para sacrificios disponibles. Sigue misma lógica del 
        indicador de turno. Ejemplo en pantalla:
          * 'Sacrificios: 5'"""
        self.textTrib1 = tk.StringVar()
        self.textTrib2 = tk.StringVar()
        self.textTrib1.set(str(self.j1.sacrificios))
        self.textTrib2.set(str(self.j2.sacrificios))
        self.Trib1Display = tk.Label(self.cv, textvariable = self.textTrib1)
        self.Trib1Display.place (x = 520, y = 761, anchor = tk.NW)
        self.Trib2Display = tk.Label(self.cv, textvariable = self.textTrib2)
        self.Trib2Display.place (x = 1020, y = 761, anchor = tk.NW)
        self.Trib1Head = tk.Label(self.cv, text = 'Sacrificios: ')
        self.Trib1Head.place(x = 420, y= 761, anchor = tk.NW)
        self.Trib2Head = tk.Label(self.cv, text = 'Sacrificios: ')
        self.Trib2Head.place(x = 920, y= 761, anchor = tk.NW)

        """Construcción de botones. Cada botón se construye de manera similar y
        representa las acciones disponibles de ambos jugadores. Se tomará el
        botón de ataque del j1 para explicar construcción.
        """
        # Creación botón juntoa texto presentado
        self.boton1 = tk.Button(self.cv, text="Atacar")
        # Ancho y color de fondo
        self.boton1.configure(width=10, activebackground="white")
        # Disposición en canvas
        self.boton1_window = self.cv.create_window(420, 700, anchor=tk.NW, window=self.boton1)
        # Event binding -> llamar función al ser clickeado
        self.boton1.bind('<Button-1>', self.attackA)

        # Sacrificio j1
        self.boton2 = tk.Button(self.cv, text="Sacrificar")
        self.boton2.configure(width=10, activebackground="white")
        self.boton2_window = self.cv.create_window(520, 700, anchor=tk.NW, window=self.boton2)
        self.boton2.bind('<Button-1>', self.tributeA)

        # Ataque j2
        self.boton3 = tk.Button(self.cv, text="Atacar")
        self.boton3.configure(width=10, activebackground="white")
        self.boton3_window = self.cv.create_window(920, 700, anchor=tk.NW, window=self.boton3)
        self.boton3.bind('<Button-1>', self.attackB)

        # Sacrificio j2
        self.boton4 = tk.Button(self.cv, text="Sacrificar")
        self.boton4.configure(width=10, activebackground="white")
        self.boton4_window =self.cv.create_window(1020, 700, anchor=tk.NW, window=self.boton4)
        self.boton4.bind('<Button-1>', self.tributeB)

    def attackA(self, event):
        """Método encargado de gestionar la lógica del ataque del jugador 1.

        El proceso del ataque de un jugador a otro corresponde al siguiente.
            * Se verifica que el turno actual corresponda al jugador invocando
              el ataque. Si es caso opuesto, no se realiza acción.
            * Se compara el ATK de la carta del jugador con la defensa de la
              carta del oponente.
            * Si ATK>DEF: Oponente recibe daño y cambia su carta actual
            * Si ATK<DEF: Jugador recibe daño y cambia su carta actual
            * Si ATK=DEF: Ambos jugadores cambian su carta actual.
        
        Args:
            event : Requerido por Tkinter para "Event Binding"
        """
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
            # Enzi: "Recargamos las cartas, actualizamos turno, revisamos si 
            #       hay ganador y actualizamos canvas"
            self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
            self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')
            self.turno = "j2"
            self.checkear()
            self.textTurno.set(self.turno)
            self.cv.update()

    def attackB(self, event):
        """Método encargado de gestionar la lógica del ataque del jugador 2.

        El proceso del ataque de un jugador a otro corresponde al siguiente.
            * Se verifica que el turno actual corresponda al jugador invocando
              el ataque. Si es caso opuesto, no se realiza acción.
            * Se compara el ATK de la carta del jugador con la defensa de la
              carta del oponente.
            * Si ATK>DEF: Oponente recibe daño y cambia su carta actual
            * Si ATK<DEF: Jugador recibe daño y cambia su carta actual
            * Si ATK=DEF: Ambos jugadores cambian su carta actual.
        
        Args:
            event : Requerido por Tkinter para "Event Binding"
        """
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
            # Enzi: "Recargamos las cartas, actualizamos turno, revisamos si 
            #       hay ganador y actualizamos canvas"
            self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
            self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')
            self.turno = "j1"
            self.checkear()
            self.textTurno.set(self.turno)
            self.cv.update()

    def tributeA(self, event):
        """Método encargado de gestionar la lógica de sacrificio del jugador 1.

        El proceso de sacrificio de la carta actual de un jugador corresponde a:
            * Se verifica que el turno actual corresponda al jugador invocando
              el sacrificio. Si es caso opuesto, no se realiza acción.
            * Se verifica si el jugador dispone de sacrificios. Si ya no posee
              mas sacrificios, no se realizan cambios. Revisar documentación de
              método 'jugador.UseTribute'
            * Se reduce en 1 el contador de sacrificios del jugador, y se 
              realiza cambio de carta activa.
        Args:
            event : Requerido por Tkinter para "Event Binding"
        """
        # Check de turno
        if self.turno == "j1":
            self.j1.UseTribute(self.diccionario)
            self.textTrib1.set(str(self.j1.sacrificios))
            # Enzi: "Recargamos la carta, actualizamos turno y actualizamos canvas"
            self.cv.create_image(300, 10, image=self.j1.card.photo, anchor='nw')
            self.turno = "j2"
            self.textTurno.set(self.turno)
            self.cv.update()

    def tributeB(self, event):
        """Método encargado de gestionar la lógica de sacrificio del jugador 2.

        El proceso de sacrificio de la carta actual de un jugador corresponde a:
            * Se verifica que el turno actual corresponda al jugador invocando
              el sacrificio. Si es caso opuesto, no se realiza acción.
            * Se verifica si el jugador dispone de sacrificios. Si ya no posee
              mas sacrificios, no se realizan cambios. Revisar documentación de
              método 'jugador.UseTribute'
            * Se reduce en 1 el contador de sacrificios del jugador, y se 
              realiza cambio de carta activa.
        Args:
            event : Requerido por Tkinter para "Event Binding"
        """
        if self.turno == "j2":
            self.j2.UseTribute(self.diccionario)
            self.textTrib2.set(str(self.j2.sacrificios))
            # Enzi: "Recargamos la carta, actualizamos turno y actualizamos canvas"
            self.cv.create_image(800, 10, image=self.j2.card.photo, anchor='nw')
            self.turno = "j1"
            self.textTurno.set(self.turno)
            self.cv.update()

    def checkear(self):
        """Llamada para revisar si alguno de los jugadores perdió todos sus
        puntos de vida en cada término de turno."""
        if self.j1.getVida() == 0:
            self.textVictoria.set("Jugador 2 ha Ganado \n puede salir del juego")
            self.turno = "Fin Partida"
            self.cv.update()
        elif self.j2.getVida() == 0:
            self.textVictoria.set("Jugador 1 ha Ganado \npuede salir del juego")
            self.turno = "Fin Partida"
            self.cv.update()


