
# Cerinta 2 - Citirea unui sir din fisier

nume_fisier =input("Introdu numele fisierului: ")

try:
    with open(nume_fisier, "r", encoding="utf-8") as fisier:
        continut = fisier.read()

    sir = [int(numar) for numar in continut.split()]

    print("\nSirul citit din fisier este:")
    print(*sir)

except FileNotFoundError:
    print("Eroare: Fisierul nu exista!")

except ValueError:
    print("Eroare: Fisierul trebuie sa contina numere intregi!")
