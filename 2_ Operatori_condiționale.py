'''
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.
    If else evaluează condiții și bifurcă codul în funcție de rezultat.
Flow control - codul ,,curge" după condițiile stabilite de noi.
Dacă (if) condiția este îndeplinită atunci execută ceva, altfel (else) execută altceva.
'''

# 2. Verifică și afișează dacă x este număr natural sau nu.

x = int(input())
if x >= 0 :
    print(f"{x} este număr natural")
else:
    print(f"{x} nu este număr natural")

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# x = int(input())
# if x > 0 :
#     print(f"{x} este număr pozitiv")
# elif x == 0:
#     print(f"{x} este număr neutru")
# else:
#     print(f"{x} este număr negativ")

# 4. Verifică și afișează dacă x este între -2 și 13.

# x = int(input())
# if -2 < x and x < 13:
#     print(f"{x} este între -2 și 13")
# else:
#     print(f"{x} nu este între -2 și 13")

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

# x = int(input())
# y = int(input())
# if (x-y)<5:
#     print(f"Diferența dintre {x} și {y} este mai mică de 5")
# else:
#     print(f"Diferența dintre {x} și {y} nu este mai mică de 5")

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

# x = int(input())
# if (not (5 < x and x < 27)):
#     print(f"{x} nu este între 5 și 27")
# else:
#     print(f"{x} este între 5 și 27")

'''
7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''

# x = int(input())
# y = int(input())
# if x > y :
#     print(f"{x} este mai mare ca {y}")
# elif x == y:
#     print(f"{x} și {y} sunt egale")
# else:
#     print(f"{y} este mai mare ca {x}")

'''
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
# x = int(input())
# y = int(input())
# z = int(input())
# if x == y == z :
#     print('Triunghiul este echilateral')
# elif x == y or x == z or y == z:
#     print('Triunghiul este isoscel')
# else:
#     print('Triunghiul este oarecare')

'''
9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu.
'''
# x = str(input())
# if x == 'a' or x == 'A':
#     print(f'{x} este vocală')
# elif x == 'e' or x == 'E':
#     print(f'{x} este vocală')
# elif x == 'i' or x == 'I':
#     print(f'{x} este vocală')
# elif x == 'o' or x == 'O':
#     print(f'{x} este vocală')
# elif x == 'u' or x == 'U':
#     print(f'{x} este vocală')
# elif x == 'ă' or x == 'Ă':
#     print(f'{x} este vocală')
# elif x == 'â' or x == 'Â':
#     print(f'{x} este vocală')
# elif x == 'î' or x == 'Î':
#     print(f'{x} este vocală')
# else:
#     print(f'{x} nu este vocală')

'''
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
# x = int(input())
# if x > 9:
#     print('Ai luat nota A')
# elif x > 8:
#     print('Ai luat nota B')
# elif x > 7:
#     print('Ai luat nota C')
# elif x > 6:
#     print('Ai luat nota D')
# elif x > 4:
#     print('Ai luat nota E')
# else:
#     print('Ai luat nota F')
