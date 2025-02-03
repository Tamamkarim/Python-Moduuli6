import random

def heitä_noppaa():
    return random.randint(1, 6)

def pääohjelma():
    while True:
        silmäluku = heitä_noppaa()
        print(silmäluku)
        if silmäluku == 6:
            break

if __name__ == "__main__":
    pääohjelma()
