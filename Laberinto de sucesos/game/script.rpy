# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#DeLunna
define Tormenta = Character("Tormenta", color = "#75dfff")
define Luke = Character("Luke", color = "#4b0082")
define Alma = Character ("Alma", color = "#8b3a3a")
define Lia = Character ("Lia", color = "#fff0f5")
define Dimitruk = Character("Dimitruk", color = "#cdc5bf")

#Fenix
define Lilith = Character("Lilith", color = "#b57edc")
define Arleth = Character("Arleth", color = "#ff91af")
define Atenea = Character("Atenea", color = "#df73ff")
define Kenneth = Character("Kenneth", color = "#00a86b")

#Nieves
define Dimitra = Character("Dimitra", color = "#ff55a3")
define Keithlyn = Character("Keithlyn", color = "#f4c2c2")
define Allen = Character("Allen", color = "#fd6c9e")
define Kay = Character("Kay", color = "#fa8072")
define Heather = Character("Heather", color = "#f38fa9")
define Loren = Character("Loren", color = "#9f00ff")
define Hellen = Character("Hellen", color = "#ff43a4")
#faltan las 4 hermanas

#Skylar
define Rayo = Character("Rayo", color = "#318ce7")
define Trueno = Character("Trueno", color = "#66ddaa")
define Kann = Character("Kann", color = "#8b4513")
define Dimitri = Character("Dimitri", color = "#1560bd")
define Keyla = Character("Keyla", color = "#aaf0d1")

#Grupos
define Lluvia = Character("Lluvia", color = "#8806ce")
define Rex = Character("Rex", color = "#ff0000")
define Nightmare = Character("Nightmare", color = "#4166f5")
define Darek = Character("Darek", color = "#ffdf00")
define Dominik = Character("Dominik", color = "#00ff00")
define Terri = Character("Terri", color = "#ed2939")
define Genesis = Character("Yen", color = "#a8e4a0")

#Desconocido
define Aira = Character("???", color = "#fc8eac")
define Alba = Character("???", color = "#ff3030")
define Aura = Character("???", color = "#7fffd4")


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
    jump chapter1


    # Finaliza el juego:

    return
