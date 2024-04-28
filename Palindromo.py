"""
PSEUDOCÓDIGO:
Algoritmo palindromo 
-Hipótesis: 
    Verificar frases para saber si son palindromo
-Precondición:
    Utilizar unicode para los caracteres
-Entrada: 
    Frase
-Tratamiento datos:
    Filtrar caracteres unicamente(quitar espacios) y tildes (NFD)
    Convertir a mayúsculas o minúsculas
    Verificar palindromo

-Salida:
    Booleano (True: Palindromo, False: NotPalindromo)
"""
import unicodedata

# Función para normalizar el texto eliminando acentos y convirtiendo letras a mayúsculas
import unicodedata

# Función para normalizar el texto eliminando acentos y convirtiendo letras a mayúsculas
def normalizar_texto(text):
    normalized_text = ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn' and char.isalnum()).upper() #Ayuda chatGPT
    return normalized_text

# Función para verificar si un texto es un palíndromo
def es_palindromo(text):
    normalized_text = normalizar_texto(text)  # Normaliza el texto
    return normalized_text == normalized_text[::-1]  # Comparamos el texto con su reverso para determinar si es un palíndromo

# Función principal del programa
def main():
    print("Bienvenido")
    while True:
        print("Menú:")
        print("1. Ingresar una frase")
        print("2. Salir")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            frase = input("Ingrese su frase: ")  # Solicitamos al usuario que ingrese una frase
            if es_palindromo(frase):  # Verificamos si la frase es un palíndromo
                print("La frase es un palíndromo")  # Imprimimos un mensaje si la frase es un palíndromo
            else:
                print("La frase no es un palíndromo.")  # Imprimimos un mensaje si la frase no es un palíndromo
        elif eleccion == "2":
            print("¡Hasta luego!")  # Mensaje de despedida si el usuario elige salir del programa
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")  # Mensaje si el usuario elige una opción no válida

# Ejecutamos la función principal del programa
if __name__ == "__main__":
    main()
