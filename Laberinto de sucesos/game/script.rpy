# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
#DeLunna
define Tormenta = Character("Tormenta", color = "#75dfff")
define Luke = Character("Luke", color = "#4b0082")
define Alma = Character ("Alma", color = "#8b3a3a")

#Fenix
define Lilith = Character("Lilith", color = "#8a2be2")
define Arleth = Character("Arleth", color = "#ff91af")

#Nieves
define Dimitra = Character("Dimitra", color = "#ff55a3")

#Skylar



# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
