"""Kirjoita funktio, joka saa parametrinaan
listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä
alkuperäisen että karsitun listan."""


def poista(kokonaisluvut):
    return [luku for luku in kokonaisluvut if luku % 2 != 0]

def pää():
    alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = poista(alkuperäinen_lista)
    print(f"Alkuperäinen lista: {alkuperäinen_lista}")
    print(f"Karsittu lista: {karsittu_lista}")

