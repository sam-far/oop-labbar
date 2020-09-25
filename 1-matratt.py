class Matratt():
    def __init__(self, namn, pris, typ, kalorier):
        self.namn = namn
        self.pris = pris
        self.typ = typ
        self.kalorier = kalorier

if __name__ == "__main__":
    
    mat = Matratt("Flygande Jakob", 100, "Kött", 2000)
    mat2 = Matratt("Vegansk paj", 120, "Vegansk", 1400)
    mat3 = Matratt("Caesarsallad", 110, "Vegetarisk", 1500)

    print(
        f"\n{mat.namn}\n{mat.pris} Kr\n{mat.typ} Rätt\n{mat.kalorier} Kalorier\n"
        f"\n{mat2.namn}\n{mat2.pris} Kr\n{mat2.typ} Rätt\n{mat2.kalorier} Kalorier\n"
        f"\n{mat3.namn}\n{mat3.pris} Kr\n{mat3.typ} Rätt\n{mat3.kalorier} Kalorier\n"
    )