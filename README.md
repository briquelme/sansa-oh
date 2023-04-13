# sansa-oh
Simple juego de cartas escrito en Python, usando imágenes e in-jokes de los autores.


## Creditos
El programa fue desarrollado por Benjamín Riquelme (briquelme) y Gabriel Ortega (Enzi-Rogue). Las imágenes fueron construidas usando la herramienta [Yu-Gi-Oh! card maker](https://www.cardmaker.net/yugioh/).

## Reglas del juego

Cada jugador posee puntos de vida, puntos de sacrificio y una carta activa. Los puntos de sacrificio corresponden a la mitad de los puntos de vida iniciales, truncando el valor a la unidad.

Durante su turno, el jugador puede tomar dos acciones:
- Atacar. El jugador envia su carta activa a combatir la carta del oponente. Para determinar cual de las dos cartas resulta victoriosa, se compara el ATK del atacante con la DEF del oponente. La carta cuyo valor sea menor será destruida, reemplazada por una nueva y su dueño recibirá 1 punto de daño.
- Sacrificar. El jugador consume 1 punto de sacrificio para poder destruir su carta actual y recibir una nueva. En caso de no poseer puntos de sacrificio, el jugador termina su turno sin cambiar su carta.

El juego termina cuando los puntos de vida de uno de los jugadores llegue a 0.


## Uso
Primera instancia, crear un entorno de Python que contenga los paquetes indicados en el archivo `requirements.txt`. En la carpeta `img` se dispone de cartas ya creadas para poder iniciar una partida lo más pronto posible.

Utilizar `python ./main.py` para iniciar el programa. En consola, se le pedirá ingresar la cantidad de vidas de los jugadores, y cual de los dos jugadores tendrá el primer turno. Cerrar la ventana terminará con la ejecución del programa.

### Agregar nuevas cartas.
La carpeta `img` almacena los archivos relacionados a las cartas disponibles en el juego. 
#### Manejo de lista de cartas
El archivo `cartas.txt` actua como base de datos de las cartas disponibles, donde cada linea corresponde a una carta y sigue el siguiente formato: `<nombre> <atk> <def>`. El significado de cada columna corresponde a:
- `<nombre>`: nombre de la imagen asociada a la carta. No debe poseer la extensión del archivo.
- `<atk>`: valor de ATK de la carta. Se espera un número entero como valor.
- `<def>`: valor de DEF de la carta. Se espera un número entero como valor.
#### Manejo de imágenes de cartas.
Para cada carta registrada en la lista de cartas, debe existir una imagen con el nombre indicado dentro de la carpeta `img`. Nuevas imágenes pueden ser generadas con la herramienta [Yu-Gi-Oh! card maker](https://www.cardmaker.net/yugioh/) y deben ser almacenadas en formato `jpg`, usando dicha extensión y con dimensiones `419x610`.
