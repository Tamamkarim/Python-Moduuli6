def poista_parittomat(kokonaisluvut):
    return [luku for luku in kokonaisluvut if luku % 2 != 0]

def pääohjelma():
    alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = poista_parittomat(alkuperäinen_lista)
    print(f"Alkuperäinen lista: {alkuperäinen_lista}")
    print(f"Karsittu lista: {karsittu_lista}")

if __name__ == "__main__":
    pääohjelma()
