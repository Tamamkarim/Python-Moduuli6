"""Kirjoita parametriton funktio, joka palauttaa
paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes
tulee kuutonen. Pääohjelma tulostaa kunkin
 heiton jälkeen saadun silmäluvun. """

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
