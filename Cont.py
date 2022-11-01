'''
4.Clasa Cont

Atribute: iban, titular_cont, sold
Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

class Cont:

    # atributele obiectelor de tip Cont
    def __init__(self, iban_p, titular_cont_p, sold_p):
        self.iban = iban_p
        self.titular_cont = titular_cont_p
        self.sold = sold_p

    # metoda afisare_sold
    def afisare_sold(self):
        return (f"\nTitularul {self.titular_cont}, are in contul {self.iban}, suma de {self.sold} lei")

    # metoda debitare_cont
    def debitare_cont(self, bani):
        self.sold = self.sold - bani

    # metoda creditare_cont
    def creditare_cont(self, bani):
        self.sold = self.sold + bani

if __name__ == "__main__":

    c1 = Cont(987652347645, "Popescu Ion", 567.03)
    print(c1.afisare_sold())
    c1.debitare_cont(560)
    print(c1.afisare_sold())
    c1.creditare_cont(700)
    print(c1.afisare_sold())

