import random

def heitä_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

def pääohjelma():
    tahkojen_maara = int(input("Syötä nopan tahkojen määrä: "))
    maksimisilmäluku = int(input(f"Syötä nopan maksimisilmäluku (1–{tahkojen_maara}): "))

    while True:
        silmäluku = heitä_noppaa(tahkojen_maara)
        print(silmäluku)
        if silmäluku == maksimisilmäluku:
            break


if __name__ == "__main__":
    pääohjelma()
