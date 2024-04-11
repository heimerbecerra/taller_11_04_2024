'''
Ejercicio 3: Registro de Estudiantes 
Enunciado: 
Crea un programa en Python que permita al usuario registrar información de estudiantes. El 
programa debe solicitar al usuario que ingrese el nombre, la edad y la carrera de cada estudiante. 
Luego, el usuario debe poder buscar un estudiante por su nombre y ver su información 
correspondiente. 

'''

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

class RegistroEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                return estudiante
        return None

def menu():
    print("\n--- Menú ---")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Salir")

if __name__ == "__main__":
    registro = RegistroEstudiantes()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            carrera = input("Ingrese la carrera del estudiante: ")
            estudiante = Estudiante(nombre, edad, carrera)
            registro.agregar_estudiante(estudiante)
            print("Estudiante agregado al registro.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            estudiante_encontrado = registro.buscar_estudiante(nombre)
            if estudiante_encontrado:
                print(f"Información del estudiante:")
                print(f"Nombre: {estudiante_encontrado.nombre}")
                print(f"Edad: {estudiante_encontrado.edad}")
                print(f"Carrera: {estudiante_encontrado.carrera}")
            else:
                print("Estudiante no encontrado en el registro.")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
