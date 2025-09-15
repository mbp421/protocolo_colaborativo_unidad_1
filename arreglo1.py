import random

# 1. Declaracion y creacion de arreglo
numeros = [random.randint(0, 99) for _ in range(10)]
print("Arreglo inicial:", numeros)

# 2. Recorrido
print("\nRecorrido con for clasico:")
for i in range(len(numeros)):
    print(numeros[i], end=" ")
print()

print("Recorrido con for-each:")
for n in numeros:
    print(n, end=" ")
print("\n")

# 3. Modificacion
# Cambiar impares por 0
numeros = [0 if n % 2 != 0 else n for n in numeros]
print("Arreglo con pares = 0:", numeros)

# Multiplicar por indice
numeros = [n * i for i, n in enumerate(numeros)]
print("Arreglo multiplicado por indice:", numeros)

# 4. Busqueda
valor = 2
encontrado = valor in numeros
print(f"El valor {valor} esta en el arreglo?:", encontrado)
