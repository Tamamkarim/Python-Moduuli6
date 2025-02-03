def laske_summa(kokonaisluvut):
    summa = 0
    for luku in kokonaisluvut:
        summa += luku
    return summa

def pääohjelma():
    luvut = [1, 2, 3, 4, 5]
    summa = laske_summa(luvut)
    print(f"Listan lukujen summa on: {summa}")

if __name__ == "__main__":
    pääohjelma()
