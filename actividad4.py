# Definir una lista de diccionarios para almacenar la información de las películas
peliculas = []

# Función para registrar la información de una película
def registrar_pelicula():
    titulo = input("Ingrese el título de la película: ")
    genero = input("Ingrese el género de la película: ")
    anio = int(input("Ingrese el año de la película: "))
    pelicula = {
        "titulo": titulo,
        "genero": genero,
        "anio": anio
    }
    peliculas.append(pelicula)
    print("Información de la película registrada con éxito.")

# Función para buscar una película por su título
def buscar_pelicula():
    titulo = input("Ingrese el título de la película que desea buscar: ")
    encontrado = False
    for pelicula in peliculas:
        if pelicula["titulo"] == titulo:
            print("Título:", pelicula["titulo"])
            print("Género:", pelicula["genero"])
            print("Año:", pelicula["anio"])
            encontrado = True
            break
    if not encontrado:
        print("No se encontró la película en la lista.")

# Menú principal
while True:
    print("\n==== Menú ====")
    print("1. Registrar película")
    print("2. Buscar película")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_pelicula()
    elif opcion == "2":
        buscar_pelicula()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

print("Gracias por usar el programa. ¡Hasta luego!")