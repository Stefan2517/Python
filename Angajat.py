'''
3.Clasa Angajat

Atribute: nume, prenume, salariu
Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''
class Angajat:
    # atributele obiectelor de tip Angajat
    def __init__(self, nume_p, prenume_p, salariu_p):
        self.nume = nume_p
        self.prenume = prenume_p
        self.salariu = salariu_p

        # metoda descrie
    def descrie(self):
        return (f'\nAngajatul are numele {self.nume}, prenumele {self.prenume}, si salariul {self.salariu}')
        # metoda pentru nume complet

    def nume_complet(self):
        return (f'\nNumele complet al angajatului este {self.nume} {self.prenume}')
        # metoda pentru salariu lunar

    def salariu_lunar(self):
        return (f'\nSalariul lunar al angajatului este {self.salariu}')
        # metoda pentru salariu anual

    def salariu_anual(self):
        return (f'\nSalariul anual al angajatului este {12* self.salariu}')
    # marire_salariu(procent)
    def marire_salariu(self, procent):
        self.salariu = self.salariu + (self.salariu*procent/100)


if __name__ == "__main__":
    angajat = Angajat("Semelbauer", "Stefan", 2400)
    print(angajat.descrie())
    print(angajat.nume_complet())
    print(angajat.salariu_lunar())
    print(angajat.salariu_anual())
    angajat.marire_salariu(5)
    print(angajat.descrie())