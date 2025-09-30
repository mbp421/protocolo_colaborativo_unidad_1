import random
import bisect
import time

# Algoritmos de busqueda
def busqueda_lineal(lista, clave):
    for i, valor in enumerate(lista):
        if valor == clave:
            return i
    return -1

def busqueda_binaria(lista, clave):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == clave:
            return medio
        elif lista[medio] < clave:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Algoritmos de ordenamiento
def ordenamiento_burbuja(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenamiento_insercion(lista):
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + centro + quicksort(derecha)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Juego del ahorcado
def obtener_palabra_aleatoria():
    palabras = ["materia", "comida", "agua", "gato", "felicidad", "saltar", "futbol"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
    print(tablero)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = 10
    letras_ordenadas = sorted(set(palabra_secreta))

    print("\n JUEGO DEL AHORCADO CON BUSQUEDAS \n")
    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Escribe una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has ingresado esta letra cachon, intenta con otra.\n")
            continue

        pos_lineal = busqueda_lineal(list(palabra_secreta), letra)
        pos_binaria = busqueda_binaria(letras_ordenadas, letra)

        if pos_lineal != -1:
            letras_adivinadas.append(letra)
            print(f"La letra '{letra}' encontrada con busqueda lineal en {pos_lineal}.")
            print(f"Tambien verificada con busqueda binaria en indice {pos_binaria}.\n")
            if set(palabra_secreta).issubset(set(letras_adivinadas)):
                print(f"Ganaste! La palabra era: {palabra_secreta}")
                break
        else:
            intentos_restantes -= 1
            print(f"Nadaaaa esa no era. Te quedan {intentos_restantes} intentos.\n")

    if intentos_restantes == 0:
        print(f"Perdiste, no te dio el coco. La palabra era: {palabra_secreta}")

# Comparacion de algoritmos

def comparar_algoritmos():
    print("\n COMPARACION DE ALGORITMOS DE ORDENAMIENTO ")
    numeros = [random.randint(0, 9999) for _ in range(2000)]  # lista grande para medir eficiencia

    for nombre, funcion in [
        ("Burbuja", ordenamiento_burbuja),
        ("Insercion", ordenamiento_insercion),
        ("Quicksort", quicksort),
        ("Mergesort", mergesort),
        ("sorted()", sorted)
    ]:
        inicio = time.time()
        funcion(numeros)
        fin = time.time()
        print(f"{nombre:10} -> Tiempo: {fin - inicio:.5f} segundos")

    print("\nConclusion: Burbuja e Insercion son O(n^2) y lentos en listas grandes. Quicksort y Mergesort (O(n log n)) son mucho mas eficientes. Por eso optimizamos reemplazando Burbuja por Quicksort.")

# 
# Programa principal
if __name__ == "__main__":
    jugar_ahorcado()
    comparar_algoritmos()
