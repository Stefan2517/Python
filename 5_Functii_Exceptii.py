# 1. Functie care sa calculeze si sa returneze suma a 2 numere

# def suma_numere(x, y):
#     z = (x + y)
#     return z
#
# if __name__ == "__main__":
#     a = int(input("a = "))
#     b = int(input("b = "))
#     sum = suma_numere(a, b)
#     print(f"suma numerelor este = {sum}")

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

# def numar(x):
#     if x % 2:
#         return False
#     else:
#         return True
#
# if __name__ == "__main__":
#     a = int(input("a = "))
#     z = numar(a)
#     print(z)

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

# def nr_carectere(re, ri, ra):
#     re = len(nume)
#     ri = len(prenume)
#     ra = len(nume_mijlociu)
#     caractere = (ri + re + ra)
#     return caractere
#
# if __name__ == "__main__":
#     nume = str(input("nume = "))
#     prenume = str(input("prenume = "))
#     nume_mijlociu = str(input("nume_mijlociu = "))
#     z = nr_carectere(nume, prenume, nume_mijlociu)
#     print(z)

# 4. Functie care returneaza aria dreptunghiului

# def aria(x, y):
#     z = (x * y)
#     return z
#
# if __name__ == "__main__":
#     a = int(input("Introduceti va rog lungimea dreptunghiului = "))
#     b = int(input("Introduceti va rog latimea dreptunghiului = "))
#     arie = aria(a, b)
#     print(f"Aria dreptunghiului este = {arie}")

# 5. Functie care returneaza aria cercului
# pi = 3.14159
# def aria1(x):
#     z = ((x**2)*pi)
#     return z
#
# if __name__ == "__main__":
#     a = int(input("Introduceti va rog raza cercului = "))
#     arie1 = aria1(a)
#     print(f"Aria dreptunghiului este = {arie1} ")

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
# def caracter(x, y):
#     if x.count(y):
#         return True
#     else:
#         return False
#
# if __name__ == "__main__":
#     a = str(input("Introduceti un string = "))
#     b = str(input("Introduceti caracterul dorit pe care sa-l caut = "))
#     z = caracter(a,b)
#     print(z)

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case este y

# def caracter(x):
#     Majuscule = [h for h in x if h.isupper()]
#     print(f"Nr de caractere upper case este: {len(Majuscule)}")
#
#     lower_case = [k for k in x if k.islower()]
#     print(f"Nr de caractere lower case este: {len(lower_case)}")
# if __name__ == "__main__":
#     a = str(input("Introduceti un string = "))
#     z = caracter(a)

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
#
# def func(l):
#     l = []
#     for i in range(0, cate):
#         numere = int(input())
#         l.append(numere)
#
#     p = []
#     for k in l:
#         if k > 0:
#             p.append(k)
#     return p
#
# if __name__ == "__main__":
#     cate = int(input("Introduceti cate numere doriti sa contina lista: "))
#     pozitive = func(cate)
#     print(f"LISTA doar cu numerele pozitive = {pozitive} ")

# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# -	Primul numar x este mai mare decat al doilea nr y
# -	Al doilea nr y este mai mare decat primul nr x
# -	Numerele sunt egale.

# def nr(x, y):
#     if x<y:
#         print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
#     elif x==y:
#         print("Numerele sunt egale.")
#     else:
#         print(f"Primul numar {x} este mai mare decat al doilea nr {y}")
#
#
# if __name__ == "__main__":
#     a = int(input("Introduceti primul numar: "))
#     b = int(input("Introduceti al doilea numar: "))
#     z = nr(a,b)

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

# def nr(l, k):
#     l = []
#     for i in range(0, b):
#         numere = int(input())
#         l.append(numere)
#     k = set(l)
#     g_init = len(k)
#     k.add(a)
#     g_fin = len(k)
#     if g_fin > g_init:
#         print('Am adaugat numarul nou in set')
#         return True
#     else:
#         print('Nu am adaugat numarul in set. Acesta exista deja')
#         return False
#
# if __name__ == "__main__":
#     a = int(input("Introduceti un numar: "))
#     b = int(input("Introduceti cate numere doriti sa contina set-ul, apoi respectivele numere: "))
#     z = nr(a,b)
#     print(z)
