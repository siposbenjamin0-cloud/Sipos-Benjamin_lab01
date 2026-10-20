
# Cerinta 1 - Citirea datelor de la tastatura

# Citirea unui sir de numere
n = int(input("Cate numere are sirul? "))

sir = []

for i in range(n):
    numar = int(input(f"Introdu numarul {i + 1}: "))
    sir.append(numar)

print("\nSirul introdus este:", sir)


# Citirea unei matrice
linii = int(input("\nNumarul de linii: "))
coloane = int(input("Numarul de coloane: "))

matrice = []

for i in range(linii):
    rand = []
    for j in range(coloane):
        numar = int(input(f"Elementul [{i + 1}][{j + 1}]: "))
        rand.append(numar)
    matrice.append(rand)


# Afisarea matricei
print("\nMatricea introdusa este:")

for rand in matrice:
    print(*rand)

