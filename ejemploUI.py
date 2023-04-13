"""Archvio de prototipo para la interfaz, presentando la carga de imágenes de 
cartas junto a botones de jugadas disponibles. No presenta funcionalidad al 
proyecto final, pero puede ser usado de ejemplo.
"""
import tkinter as tk
from PIL import Image,ImageTk
# Creación Ventana
root = tk.Tk()
root.title("display image")
# Carga de imágenes de cartas
im=Image.open("./img/enzi.jpg")
im2 = Image.open("./img/camilo.jpg")
photo=ImageTk.PhotoImage(im)
photo2 = ImageTk.PhotoImage(im2)
# Configuración canvas
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
# Agregar imágenes en coordenadas indicadas dentro de canvas.
cv.create_image(300, 10, image=photo, anchor='nw')
cv.create_image(800,10,image=photo2,anchor='nw')

#Distribución de botones

#Construcción de boton con texto, ancho y color fondo
boton1 = tk.Button(cv,text="Atacar")
boton1.configure(width = 10, activebackground = "white")
#Se dibuja boton en canvas, encapsulado en 'window'
boton1_window = cv.create_window(420, 700, anchor=tk.NW, window=boton1)

#Procedimiento se repite con cada boton.
boton2 = tk.Button(cv,text="Sacrificar")
boton2.configure(width = 10, activebackground = "white")
boton2_window = cv.create_window(520, 700, anchor=tk.NW, window=boton2)
boton3 = tk.Button(cv,text="Atacar")
boton3.configure(width = 10, activebackground = "white")
boton3_window = cv.create_window(920, 700, anchor=tk.NW, window=boton3)
boton4 = tk.Button(cv,text="Sacrificar")
boton4.configure(width = 10, activebackground = "white")
boton4_window = cv.create_window(1020, 700, anchor=tk.NW, window=boton4)
root.mainloop()