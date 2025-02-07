"""Kirjoita funktio, joka saa parametrinaan bensiinin
määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän
 käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa
 hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä
  syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa."""


def litroiksi(gallona):
    return gallona * 3.785411784

def pääohjelma():
    while True:
        gallona = float(input("Syötä bensiinin määrä gallonassa (negatiivinen luku lopettaa): "))
        if gallona < 0:
            break
        litra = muunna_gallona_litroiksi(gallona)
        print(f"{gallona} gallonaa on {litra:.2f} litraa.")

if __name__ == "__main__":
    pääohjelma()
