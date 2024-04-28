"""
PSEUDOCÓDIGO:
Algoritmo Bandera 
-Hipótesis: 
    Ordenar colores por rojo verde azul
-Precondición:
    tiene que ser de tipo rojo, verde o azul
-Entrada: 
    número de elementos para cada color
-Tratamiento datos: (Método de permutar)
    i -rojos
    j -verdes
    k -azules
-Salida:
    Bandera ordenada
"""
def organizar_fichas(fichas):
    # Inicializamos los índices y los subconjuntos de fichas
    i = 0  #Rojas
    j = 0  #Verdes
    k = 0  #Azules
    n = len(fichas)  # Número total de fichas
    
    # Iteramos sobre todas las fichas
    while k < n:
        if fichas[k] == "roja":
            # Si la ficha es roja, la movemos al subconjunto de fichas rojas
            fichas[i], fichas[k] = fichas[k], fichas[i]
            i += 1
            j += 1
            k += 1
        elif fichas[k] == "verde":
            # Si la ficha es verde, la movemos al subconjunto de fichas verdes
            fichas[j], fichas[k] = fichas[k], fichas[j]
            j += 1
            k += 1
        else:
            # Si la ficha es azul, simplemente avanzamos al siguiente índice
            k += 1
    
    return fichas

def menu():
    print("Menú:")
    print("1. Organizar fichas")
    print("2. Salir")

def main():
    print("Bienvenido al organizador de Dijkstra")
    while True:
        menu()
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            fichas = input("Ingrese las fichas separadas por espacios (roja / verde / azul): ").split()
            fichas_organizadas = organizar_fichas(fichas)
            print(f"Fichas organizadas: {fichas_organizadas}")
        elif eleccion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
