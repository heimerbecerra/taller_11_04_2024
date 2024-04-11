'''
Ejercicio 1: Registro de Contactos 
Enunciado: 
Escribe un programa en Python que permita al usuario registrar contactos. El programa debe 
permitir al usuario ingresar el nombre y el número de teléfono de cada contacto. Luego, el programa 
debe permitir al usuario buscar un contacto por su nombre y mostrar su número de teléfono 
correspondiente. 

'''




#diccionario 
agenda = {}

# Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto agregado con éxito.")

# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print("El contacto no se encuentra en la agenda.")

# Función principal del programa
def main():
    while True:
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono del contacto: ")
            agregar_contacto(nombre, telefono)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            buscar_contacto(nombre)
        elif opcion == '3':
            print("Gracias por usar la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Llamar a la función principal del programa
if __name__ == "__main__":
    main()


