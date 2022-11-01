'''
2. Clasa Dreptunghi

Atribute: lungime, latime, culoare
Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''

class Dreptunghi:
    # atributele obiectelor de tip Dreptunghi
    def __init__(self, lungime_p, latime_p, culoare_p):
        self.lungime = lungime_p
        self.latime = latime_p
        self.culoare = culoare_p

    # metoda descrie dreptunghi
    def descrie_dreptunghi(self):
        return (f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime}, si culoarea {self.culoare}')

    # metoda pentru arie
    def aria(self):
        return (f'Aria dreptunghiului este {(self.lungime*self.latime)}')

    # metoda pentru perimetru
    def perimetru(self):
        return (f'Perimetrul dreptunghiului este {(2*(self.lungime+self.latime))}')

    # metoda pentru schimba_culoarea(noua_culoare)
    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua

if __name__ == "__main__":
    d1 = Dreptunghi(2, 5, 'Albastru')
    d2 = Dreptunghi(3, 7, 'Verde')
    d3 = Dreptunghi(8, 4, 'Mov')

    print(d3.aria())
    print(d2.descrie_dreptunghi())
    print(d1.perimetru())
    d2.schimba_culoarea('Portocaliu')
    print(d2.descrie_dreptunghi())

