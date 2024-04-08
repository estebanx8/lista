# Definimos el nombre del archivo
archivo = "lista.txt"

# Intentamos leer los datos del archivo
try:
    with open(archivo, "r") as f:
        nombres = f.readlines()
        nombres = [nombre.strip() for nombre in nombres]
except FileNotFoundError:
    # Si el archivo no existe, creamos una lista vacía
    nombres = []

# Leemos los datos y los agregamos a la lista
for i in range(len(nombres), 4):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    nombres.append(nombre)

# Escribimos los datos en el archivo
with open(archivo, "w") as f:
    for nombre in nombres:
        f.write(f"{nombre}\n")

print("Los datos de la lista son: ", nombres)

# Preguntamos al usuario si desea cambiar algún dato de la lista
cambiar_dato = input("¿Desea cambiar algún dato de la lista? (s/n) ")
if cambiar_dato == "s":
    # Pedimos al usuario el índice del dato a cambiar
    indice = int(input("Ingrese el índice del dato a cambiar: "))
    # Pedimos al usuario el nuevo dato
    nuevo_dato = input("Ingrese el nuevo dato: ")
    # Cambiamos el dato en la lista
    nombres[indice] = nuevo_dato
    # Escribimos los datos en el archivo
    with open(archivo, "w") as f:
        for nombre in nombres:
            f.write(f"{nombre}\n")
    print("Los datos de la lista después del cambio son: ", nombres)

# Preguntamos al usuario si desea cambiar todos los datos de la lista
cambiar_todos = input("¿Desea cambiar todos los datos de la lista? (s/n) ")
if cambiar_todos == "s":
    # Pedimos al usuario los nuevos datos
    nuevos_datos = []
    for i in range(4):
        print("Ingrese los datos de la persona", i + 1)
        nuevo_dato = input("Nombre: ")
        nuevos_datos.append(nuevo_dato)
    # Cambiamos todos los datos de la lista
    nombres = nuevos_datos
    # Escribimos los datos en el archivo
    with open(archivo, "w") as f:
        for nombre in nombres:
            f.write(f"{nombre}\n")
    print("Los datos de la lista después del cambio son: ", nombres)

# Preguntamos al usuario si desea eliminar todos los datos de la lista
eliminar_todos = input("¿Desea eliminar todos los datos de la lista? (s/n) ")
if eliminar_todos == "s":
    # Eliminamos todos los datos de la lista
    nombres = []
    # Escribimos los datos en el archivo
    with open(archivo, "w") as f:
        for nombre in nombres:
            f.write(f"{nombre}\n")
    print("Los datos de la lista después del cambio son: ", nombres)
