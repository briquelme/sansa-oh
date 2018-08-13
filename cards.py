from PIL import Image,ImageTk
from random import randint
def cardgen():
    archivo = open("./img/cartas.txt")
    d = {}
    cont = 0
    for linea in archivo:
        cont += 1
        val = linea.strip().split(" ")
        nom, atk, df = val
        d[cont] = nom, int(atk), int(df)
    archivo.close()
    return d,cont

def cardchooser(diccionario):
    carta = randint(1,len(diccionario))
    nombre,ataque,defensa = diccionario[carta]
    return nombre,ataque,defensa

class carta:
    def __init__(self,nombre,atk,df):
        self.nombre = nombre
        self.ataque = atk
        self.defensa = df
        self.filepath = "./img/" + self.nombre + ".jpg"
        self.im = Image.open(self.filepath)
        self.photo = ImageTk.PhotoImage(self.im)
    def getAtk(self):
        return self.ataque
    def getDef(self):
        return self.defensa
    

class jugador:
    def __init__(self,n,a,d,vida = 3):
        self.vida = vida
        self.card = carta(n,a,d)
        self.sacrificios = int(vida/2 - 1)

    def getAtk(self):
        return self.card.getAtk()
    def getDef(self):
        return self.card.getDef()
    def Hit(self):
        self.vida -= 1
    def ChangeCard(self, diccionario):
        Name, Attack, Defense = cardchooser(diccionario)
        self.card = carta(Name, Attack, Defense)
    def UseTribute(self, diccionario):
        if self.sacrificios >0:
            self.sacrificios -=1
            Name, Attack, Defense = cardchooser(diccionario)
            self.card = carta(Name, Attack, Defense)



