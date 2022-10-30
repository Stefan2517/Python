'''
    1.Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
a)	Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
b)	Faceti acelasi lucru cu un for each
c)	Faceti acelasi lucru cu un while
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for x in masini:
#     print(f'Masina mea preferata este {x}')


# for each in masini:
#     print(f'Masina mea preferata este {each}')


# i = 0
# while i < len(masini):
#   print(f'Masina mea preferata este {masini[i]}')
#   i += 1

'''
    2.Aceeasi lista
Folositi un for
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei
'''
# a, *b, c = masini
# lista_finala = []
# f = ' '.join(b)
# for x in f:
#     print(f'Masina mea preferata este {f}')
# d = f.lower()
# lista_finala = a + ' '+ d +' '+ c
# print(lista_finala)

'''
    3. Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
'''
# for i in masini:
#     print(f'Deocamdata am gasit {i}')
#     if i  == 'Mercedes':
#         print('Am gasit masina dorita de dvs')
#         break
#     else:
#         print(f"Am gasit masina {i}. Mai cautam")

'''
    4.Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
'''
# for i in masini:
#     if i  == 'Trabant' or i == 'Lastun':
#         continue
#     print(f"S-ar putea sa va placa masina {i}")

'''
    5. Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
-	Salvati aceste masini in masini_vechi
-	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''
# masini_vechi = []
# for i in masini:
#     print(f'Deocamdata am gasit {i}')
#     if i  == 'Trabant' or i == 'Lastun':
#         masini_vechi.append(i)
# masini[5] = 'Tesla'
# masini[7] = 'Tesla'
# print(f'Masini vechi: {masini_vechi}')
# print(f'Masini noi: {masini}')

'''
    6. Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
'''
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000,
# }
# # x reprezinta bugetul clientului
# x = 15000
# masini_de_buget = []
# b = pret_masini['Dacia']
# if b < x:
#     masini_de_buget.append('Dacia')
# n = pret_masini['Lastun']
# if n < x:
#     masini_de_buget.append('Lastun')
# m = pret_masini['Opel']
# if m < x:
#     masini_de_buget.append('Opel')
# k = pret_masini['Audi']
# if k < x:
#     masini_de_buget.append('Audi')
# j = pret_masini['BMW']
# if j < x:
#     masini_de_buget.append('BMW')
# print(f'Masinile care se incadreaza in acest buget sunt {masini_de_buget}')
#
# # Iterati prin dict.items() si accesati masina si pretul
# for i in pret_masini.items():
#     print(i)
# # Printati Pentru un buget de sub 15000 euro puteti alege masina x
# for i in masini_de_buget:
#     print(f'Pentru un buget de sub 15000 euro puteti alege masina {i}')
# # Iterati prin lista
# for i in masini_de_buget:
#     print(i)

'''
    7.Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# for i in numere:
#     print(i)
# Afisati de cate ori apare 3, (nu aveti voie sa folositi count)
# b = 0
# for i in numere:
#     if i == 3:
#         b +=1
# print(b)

'''
    8. Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''
# for i in numere:
#     print(i)
# Calculati si afisati suma numerelor, (nu aveti voie sa folositi sum)
# s=0
# for i,a in enumerate(numere):
#   s+=a
# print(s)

'''
    9. Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''
# for i in numere:
#     print(i)
# numere.sort()
# print(f'Cel mai mare numar este: {numere[-1]}')

'''
    10.Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''
# for i in numere:
#     print(i)
# noua_lista = []

# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa. Ex: daca e 3, sa devina -3
# for i in numere:
#   if i > 0:
#     print(f'-{i}')
#     noua_lista.append(f'-{i}')

# # Afisati noua lista
# print(noua_lista)
