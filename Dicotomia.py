"""
PSEUDOCÓDIGO:
Algoritmo dicotomia 
-Hipótesis: 
    Encontrar c en tabla reduciendo/2 y devolver si encontrado o no
-Precondición:
    iniciar tabla no nula
    ordenar forma ascendente
-Entrada: 
    Tabla y componente a buscar
-Tratamiento datos:
    Valor de la posición de la mitad,
    Comparar si resultado menor/mayor/(c)
    Else: reducir tabla mitad correspondiente
-Salida:
    Entero(c) y posición de c 
    NotFound
"""
def dicotomia(tabla, c):
    # Precondición: asegurarse de que la tabla no esté vacía y esté ordenada de forma ascendente
    if not tabla:
        return "Tabla vacía"
    
    # Inicialización de variables
    inicio = 0
    fin = len(tabla) - 1
    
    # Búsqueda por dicotomía
    while inicio <= fin:
        # Calcular la posición de la mitad
        medio = (inicio + fin) // 2
        
        # Comparar el valor en la posición de la mitad con c
        if tabla[medio] == c:
            # Si se encuentra el valor, devolver la posición de la mitad
            return medio
        elif tabla[medio] < c:
            # Si el valor en la posición de la mitad es menor que c, buscar en la mitad derecha de la tabla
            inicio = medio + 1
        else:
            # Si el valor en la posición de la mitad es mayor que c, buscar en la mitad izquierda de la tabla
            fin = medio - 1
    
    # Si no se encuentra c en la tabla, devolver "NotFound"
    return "NotFound"

# Función para crear una lista
def crear_lista():
    lista = input("Ingresar lista en orden ascendente separada por comas: ")
    lista = lista.split(',')
    lista = [int(x) for x in lista]
    lista.sort()
    return lista

# Función para el menú
def menu():
    print("Opciones:")
    print("1. Crear lista")
    print("2. Buscar elemento en la lista")
    print("3. Salir")

# Programa principal
lista = []
opcion = 0
while opcion != 3:
    menu()
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        lista = crear_lista()
        print(f"Lista creada con éxito: {lista}")
    elif opcion == 2:
        if not lista:
            print("Error: La lista está vacía. Cree una lista primero.")
        else:
            elemento = int(input("Ingrese el elemento para buscar en la lista: "))
            resultado = dicotomia(lista, elemento)
            if resultado != "NotFound":
                print(f"El elemento {elemento} se encuentra en la posición {resultado}")
            else:
                print(f"El elemento {elemento} no se encuentra en la lista.")
    elif opcion == 3:
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")