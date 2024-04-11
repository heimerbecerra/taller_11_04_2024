# Definir una lista de diccionarios para almacenar la información de los libros
libros = []

# Función para registrar la información de un libro
def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero
    }
    libros.append(libro)
    print("Información del libro registrada con éxito.")

# Función para buscar un libro por su título
def buscar_libro():
    titulo = input("Ingrese el título del libro que desea buscar: ")
    encontrado = False
    for libro in libros:
        if libro["titulo"] == titulo:
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Género:", libro["genero"])
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el libro en el registro.")

# Menú principal
while True:
    print("\n==== Menú ====")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_libro()
    elif opcion == "2":
        buscar_libro()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

print("Gracias por usar el programa. ¡Hasta luego!")