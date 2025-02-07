"""Kirjoita funktio, joka saa parametrinaan listan
kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
palauttaman summan."""


def laske_summa(kokonaisluvut):
    summa = 0
    for luku in kokonaisluvut:
        summa += luku
    return summa

def TK():
    luvut = [1, 2, 3, 4, 5]
    summa = laske_summa(luvut)
    print(f"Listan lukujen summa on: {summa}")



