# 1 Declaracion e inicialización con valores del 1 al 9
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2.1 Recorrido: imprimir la matriz como tabla
print("Matriz original:")
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()  # salto de línea

# 2.2 Recorrido: por columnas
print("\nRecorrido por columnas:")
for j in range(len(matriz[0])):  # columnas
    for i in range(len(matriz)):  # filas
        print(matriz[i][j], end=" ")
    print()

# 3.1 Operación: suma de todos los elementos
suma = sum(sum(fila) for fila in matriz)
print("\nSuma de todos los elementos:", suma)

# 3.2 Operación: intercambiar primera fila con la última
matriz[0], matriz[-1] = matriz[-1], matriz[0]

# Mostrar matriz despues del intercambio
print("\nMatriz despues de intercambiar primera y ultima fila:")
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()
