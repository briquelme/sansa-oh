"""Código para el manejo de cartas usadas en el juego.
Se espera que las imágenes residan en la carpeta 'img/', acompañadas del
archivo 'cartas.txt'. Para mas detalles, referir al README.
"""
from PIL import Image,ImageTk
from random import randint


def cardgen():
    """Generador de diccionario de cartas, creadas a partir del archivo 'cartas.txt'. Cada carta
    tiene asociada el nombre de la imagen asociada y sus valores de ATK y DEF.

    Returns:
        Diccionario de cartas y cantidad de cartas. El diccionario representa una tabla de cartas, donde la llave corresponde
        a la posición de la fila (partiendo con 1). Cada fila es representada con una tupla que almacena el nombre de la imagen,
        valor de ATK y valor de DEF asociados a la carta. Ejemplo de diccionario generado:
            {0: ('carta1', 1000, 2000),
            1: ('carta2', 1200, 200),
            2: ('carta3', 800, 1100)}
        Tanto las llaves como los valores de ATK y DEF son almacenados como int, mientras que el nombre de imagen es almacenado como
        str. La cantidad de cartas es entregada como int, y corresponde a max(d.keys())
    """
    archivo = open("./img/cartas.txt")
    d = dict()
    cont = 0
    for linea in archivo:
        cont += 1
        # Cada linea tiene estructura '<nombre> <ATK> <DEF>\n'. Se limpia linea
        val = linea.strip().split(" ")
        nom, atk, df = val
        # <nro_linea>:<nombre>, <ATK>, <DEF>
        d[cont] = nom, int(atk), int(df)
    archivo.close()
    return d,cont

def cardchooser(diccionario):
    """Selecciona al azar una de las cartas disponibles en el mazo indicado

    Args:
        diccionario (int:[str,int,int]): Diccionario compatible al generado por función 'cardgen'

    Returns:
        str: Nombre de imagen de carta elegida.
        int: ATK de carta elegida.
        int: DEF de carta elegida.
    """
    carta = randint(1,len(diccionario))
    # Recordar formato diccionario
    # <nro_linea>:<nombre>, <ATK>, <DEF>
    nombre,ataque,defensa = diccionario[carta]
    return nombre,ataque,defensa

class carta:
    """Clase que representa los atributos de una carta.

    Almacena datos importantes a nivel de jugabilidad (ATK y DEF) junto a elementos de la
    interfaz (directorio de imagen y estructuras para presentar la imagen en pantalla)
    
    Attributes:
        nombre(str) : nombre del archivo de imagen.
        ataque(int) : ATK.
        defensa(int) : DEF.
        filepath(str) : Dirección relativa donde reside la imagen.
        im(PIL.Image.Image) : Representación de imagen en Pillow.
        photo(PIL.ImageTk) : Representación de imagen en Pillow compatible con Tkinter
    """
    def __init__(self,nombre,atk,df):
        self.nombre = nombre
        self.ataque = atk
        self.defensa = df
        self.filepath = "./img/" + self.nombre + ".jpg"
        self.im = Image.open(self.filepath)
        self.photo = ImageTk.PhotoImage(self.im)
    def getAtk(self):
        """Método público para obtener ATK de carta
        Returns:
            int: ATK de carta
        """
        return self.ataque
    def getDef(self):
        """Método público para obtener DEF de carta
        Returns:
            int: DEF de carta
        """
        return self.defensa
    

class jugador:
    """Clase que representa los atributos de un jugador.

    Almacena datos importantes a nivel de jugabilidad, correspondiente a vida, carta actual y sacrificios disponibles

    Attributes: 
        vida (int) : Puntos de vida del jugador. Una vez llega a 0, se considera al jugador como derrotado.
        card ([str, int, int]) : Carta en juego del jugador. Corresponde a valor entregado al usar 'cardchooser'
        sacrificios (int) : Puntos de sacrificio. Al usar un punto, el jugador puede cambiar manualmente su carta en juego.
    """
    def __init__(self,n,a,d,vida = 3):
        self.vida = vida
        self.card = carta(n,a,d)
        self.sacrificios = int(vida/2)

    def getVida(self):
        return self.vida
    def getAtk(self):
        return self.card.getAtk()
    def getDef(self):
        return self.card.getDef()
    def Hit(self):
        """Aplica daño al jugador
        """
        self.vida -= 1
    def ChangeCard(self, diccionario):
        """ Cambia la carta actual del jugador por una nueva, elegida aleatoriamente desde
        el mazo suministrado. Usada solamente cuando la carta actual es destruida en batalla.
        Args:
            diccionario (int:[str,int,int]): Diccionario compatible al generado por función 'cardgen'
        """
        Name, Attack, Defense = cardchooser(diccionario)
        self.card = carta(Name, Attack, Defense)
    def UseTribute(self, diccionario):
        """ Cambia la carta actual del jugador por una nueva, elegida aleatoriamente desde
        el mazo suministrado. A diferencia del método anterior, solo puede ser usada mientras el
        jugador disponga de puntos de sacrificios. Cada invocación del método reduce en 1 el contador de
        sacrificios.
        Args:
            diccionario (int:[str,int,int]): Diccionario compatible al generado por función 'cardgen'
        """
        if self.sacrificios >0:
            self.sacrificios -=1
            Name, Attack, Defense = cardchooser(diccionario)
            self.card = carta(Name, Attack, Defense)



