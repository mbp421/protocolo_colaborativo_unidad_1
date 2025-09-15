# Declaración e inicialización con valores del 1 al 9
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Recorrido: imprimir la matriz como tabla
print("Matriz original:")
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()  # salto de línea

# Recorrido: por columnas
print("\nRecorrido por columnas:")
for j in range(len(matriz[0])):  # columnas
    for i in range(len(matriz)):  # filas
        print(matriz[i][j], end=" ")
    print()

# Operación: suma de todos los elementos
suma = sum(sum(fila) for fila in matriz)
print("\nSuma de todos los elementos:", suma)

# Operación: intercambiar primera fila con la última
matriz[0], matriz[-1] = matriz[-1], matriz[0]

# Mostrar matriz después del intercambio
print("\nMatriz después de intercambiar primera y última fila:")
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()
