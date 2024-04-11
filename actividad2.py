'''
Ejercicio 2: Inventario de Productos 
Enunciado: 
Desarrolla un programa en Python que permita al usuario mantener un inventario de productos. El 
programa debe permitir al usuario ingresar el nombre y la cantidad disponible de cada producto. 
Luego, el usuario debe poder buscar un producto por su nombre y ver cuántos están disponibles en 
el inventario

'''
class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad

    def buscar_producto(self, nombre):
        if nombre in self.inventario:
            return self.inventario[nombre]
        else:
            return 0

def menu():
    print("\n--- Menú ---")
    print("1. Agregar producto al inventario")
    print("2. Buscar producto en el inventario")
    print("3. Salir")

if __name__ == "__main__":
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad disponible: "))
            inventario.agregar_producto(nombre, cantidad)
            print("Producto agregado al inventario.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            cantidad_disponible = inventario.buscar_producto(nombre)
            print(f"Hay {cantidad_disponible} unidades de {nombre} en el inventario.")

        elif opcion == "3":
            print("¡Chao BB!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
