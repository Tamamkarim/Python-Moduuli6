def muunna_gallona_litroiksi(gallona):
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
