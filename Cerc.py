'''
1.Clasa Cerc

Atribute: raza, culoare
Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''

class Cerc:
    def __init__(self, raza_p, culoare_p):
        #atributele obiectelor de tip Cerc
        self.raza = raza_p
        self.culoare = culoare_p

    # metoda pentru descrie_cerc() - va PRINTA culoarea si raza
    def descrie_cerc(self):
        return (f"Cercul are culoarea {self.culoare} și raza: {self.raza}")

    # metoda aria() - va RETURNA aria,  pi=3,14159
    def aria(self):
        return (f'\nAria cercului este: {(3.14159*(self.raza**2))} ')

#     metoda pentru diametru()
    def diametru(self):
        return (f'\nDiametrul cercului este: {(2*self.raza)}')

#     metoda pentru circumferinta()
    def circumferinta(self):
        return (f'\nCircumferinta cercului este: {(3.14159*(self.raza*2))}')

if __name__ == "__main__":
    cerc1 = Cerc(25,'albastru')
    cerc2 = Cerc(50, 'rosu')
    cerc3 = Cerc(75,'verde')

    print(cerc1.descrie_cerc())
    print(cerc2.aria())
    print(cerc3.diametru())
    print(cerc1.circumferinta())
