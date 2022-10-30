'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

    1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o.
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.

    Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''

# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# note_muzicale = (note_muzicale[::-1])
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)

#   2. De câte ori apare ‘do’?
# print(note_muzicale.count('do'))

'''
    3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
'''
# x = [3, 1, 0, 2]
# y = [6, 5, 4]
# z = x+y
# print(z)
# x.extend(y)
# print(x)

'''
    4.
● Sortează și afișează lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
# x.sort()
# print(x)
# nu i terminat........

'''
    5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
● Lista este goală.
● Lista nu este goală.
'''
# if len(x) == 0:
#     print('Lista e goală')
# else:
#     print('Lista nu este goală')

#   6. Folosește o funcție care să șteargă lista de la exercițiul 3.
# del x[:]
# del y[:]

'''
    7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''
# if len(x) == 0:
#     print('Lista e goală')
# else:
#     print('Lista nu este goală')

'''
    8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())

'''
    9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
# x = (dict1['Ana'])
# print(f'Ana a luat {x}')
#
# y = (dict1['Gigel'])
# print(f'Gigel a luat {y}')
#
# z = (dict1['Dorel'])
# print(f'Dorel a luat {z}')

'''
    10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
# dict1['Dorel'] = 6
# print(dict1['Dorel'])

'''
    11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
# dict1.pop('Gigel')
# dict1['Ionică'] = 9
# print(dict1)