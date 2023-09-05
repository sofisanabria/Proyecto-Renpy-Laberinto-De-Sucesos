# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define diosa = DynamicCharacter("god_name", color="#6ff2a4")

define nova = Character("Nova", color="#f2ee6f")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene black background

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.

    $ god_name = "?????"

    diosa "Bienvenido."

    diosa "A partir de este momento serás presentado al mundo como Nova."

    $ god_name = "Ruby"

    diosa "Mi nombre es Ruby."

    nova "¿Dónde estoy?"

    diosa "Estás en el plano de la mente."
    diosa "Al principio podrá sonar extraño, pero aquí es donde se reúne
    todo lo que se encuentra en la existencia misma."

    menu: 
        "¿Debería preguntar?"

        "¿Por qué está todo oscuro...?":
            jump dialogo_oscuridad

        "No.":
            jump explicaciones
    

    label dialogo_oscuridad:
        nova "¿Por qué está todo oscuro si se supone que se encuentra la existencia misma aquí?"
        diosa "Tu mente aún está atada al razonamiento humano, a medida que vayas aprendiendo podrás ver aquello que es invisible para tus ojos, recuerda que todo depende de tí."

    label explicaciones:
        nova "Entiendo."
        nova "¿Entonces estoy muerto?"
        diosa "Ah, las almas humanas y la muerte."
        diosa "No es un dato relevante."
        diosa "En este momento tus objetivos serán otros, ya tendrás tiempo para descifrar tu estado físico."
        nova "¿Objetivos?"
        diosa "Sí, te he traído porque quisiera que hagas algo por mí."
        nova "¿Algo por tí?"
        diosa "Sí, te explicaré las reglas de juego:"
        diosa "Te otorgaré el poder de la omnisciencia, con la limitación de que se activará gradualmente, y aunque quieras no podrás investigarme."
        diosa "Segundo, vas a tener que observar a algunos seres terrenales, tienes prohibido interferir directamente, no deben saber que existes."
        diosa "Por último, volverás cada vez que hayas aprendido algo."
        nova "¿Cómo sabré cuándo volver?"
        diosa "Yo te traeré."
        nova "Tengo una pregunta."
        diosa "Te escucho."
        nova "¿Eres hombre o mujer?"
        diosa "Eso no es relevante."
        diosa "Si sigues buscando respuestas que concuerden con la lógica humana nunca terminarás tu misión."
        diosa "Pero respondiendo a tu pregunta:"
        diosa "Soy ambos y ninguno a la vez."


    # Finaliza el juego:

    return
