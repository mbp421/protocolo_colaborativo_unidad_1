import random

# 1. Declaración y creación de arreglo
numeros = [random.randint(0, 99) for _ in range(10)]
print("Arreglo inicial:", numeros)

# 2. Recorrido
print("\nRecorrido con for clásico:")
for i in range(len(numeros)):
    print(numeros[i], end=" ")
print()

print("Recorrido con for-each:")
for n in numeros:
    print(n, end=" ")
print("\n")

# 3. Modificación
# Cambiar impares por 0
numeros = [0 if n % 2 != 0 else n for n in numeros]
print("Arreglo con impares = 0:", numeros)

# Multiplicar por índice
numeros = [n * i for i, n in enumerate(numeros)]
print("Arreglo multiplicado por índice:", numeros)

# 4. Búsqueda
valor = 20
encontrado = valor in numeros
print(f"¿El valor {valor} está en el arreglo?:", encontrado)
