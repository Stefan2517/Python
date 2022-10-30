'''
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

    Variabila o consider ca fiind o cutie in cadrul careia pot stoca valori.
Aceasta necesita sa fie declarata si initializata.
Nu putem sa punem spatiu in denumirea variabilei.'''

'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă:
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''
# variabila string:
a = "masina"
# variabila int:
b = 25
# variabila float:
c = 3500.50
# variabila bool:
d = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(a))
print(type(b))
print(type(c))
print(type(d))

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
round(c)
print(type(c))

'''
5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.

'''
print(f'Doresc sa-mi cumpar o {a}')
print(f'Peste 4 ani voi avea {b} de ani')
print(f'Pretul acelui laptop este de {c} lei')
print(f'Masina este asigurata: {d}')

'''
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''
numele = str(input())
prenumele = str(input())
x = (len(numele + prenumele))
print(f'Numele complet are {x} caractere')

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
lungimea = int(input())
latimea = int(input())
aria = (lungimea * latimea)
print(f'Aria dreptunghiului este {aria}')

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
'''
# Din cauza neclaritatii cerintei tin sa cred ca se cere ,,the'' ca si grup de litere care apare de 3 ori.
z = 'Coral is either the stupidest animal or the smartest rock'
print(z.count('the'))

'''
9. Același string:
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
'''
# Aici cred ca se refera la cuvantul ,,the" care apare de 2 ori.
print(z.count(' the '))

'''
10. Același string:
● Folosește un assert ca să verifici dacă acest string conține doar numere.
'''
y = 'Coral is either the stupidest animal or the smartest rock'
print(y.isnumeric())

