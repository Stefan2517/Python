'''
ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
'''

from abc import abstractmethod
class FormaGeometrica:

    def __init__(self):
        self.pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        pass

'''
    INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
    ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
'''

class Patrat(FormaGeometrica):

    def __init__(self):
        self.__latura = 9

    # folosim getter sa afisam latura
    def get_latura(self):
        return self.__latura

    # folosim setter ca sa setam o alta latura
    def set_latura(self):
        self.__latura = 7

    def delete_latura(self):
        self.__latura = 0

    def descrie(self):
        print("Cel mai probabil am colturi")

    def aria(self):
        return patrat_p.get_latura() ** 2

'''
    Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
'''

class Cerc(FormaGeometrica):

    def __init__(self):
        self.__raza = 3

    # folosim getter sa afisam raza
    def get_raza(self):
        return self.__raza

    # folosim setter ca sa setam o alta raza
    def set_raza(self):
        self.__raza = 7

    def delete_raza(self):
        self.__raza = 0

    def aria(self):
        return (cerc_p.get_raza() ** 2) * clasa_abstracta.pi

    '''
    POLYMORPHISM 
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
    '''

    def descrie(self):
        print("Eu nu am colturi")


if __name__=="__main__":

    clasa_abstracta = FormaGeometrica()

    '''
Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
    '''

    patrat_p = Patrat()
    patrat_p.descrie()
    print(f"Aria primului patrat este: {patrat_p.aria()}")
    patrat_p.set_latura()
    print(f"Aria celui de al doilea patrat este: {patrat_p.aria()}")
    patrat_p.delete_latura()
    print(f"Aria celui de al treilea patrat este: {patrat_p.aria()}")

    cerc_p = Cerc()
    cerc_p.descrie()
    print(f"Aria primului cerc este : {cerc_p.aria()}")
    cerc_p.set_raza()
    print(f"Aria celui de al doilea cerc este : {cerc_p.aria()}")
    cerc_p.delete_raza()
    print(f"Aria celui de al treilea cerc este : {cerc_p.aria()}")