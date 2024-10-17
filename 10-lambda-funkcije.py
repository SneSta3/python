#anonimne ili bezimene funkcije 
# lambda argumenti: izraz

def sabiranje(x):
    return x + 50
print(sabiranje(200))
# 250

saberi = lambda x: x + 50
print(saberi(5))
# 55

lambda_sabiranje = lambda a, b: a + b
print(lambda_sabiranje(100, 200))
# 300

x = lambda a, b, c: a - b -c
print(x(100, 50, 10))
# 40

def ispitaj_broj(x):
    if x % 2 != 0:
        return True
    else:
        return False
print(ispitaj_broj(100)) #false
print(ispitaj_broj(103)) #true

ispitaj_brojeve = lambda x: x % 2 != 0
print(ispitaj_brojeve(20)) #false
print(ispitaj_brojeve(21)) #true

#sorted funkcija
lista_tuplova = [(1,5), (3, 2), (4, 1), (2, 4)]
sortirano = sorted(lista_tuplova, key=lambda x: x[1])
print(sortirano)
# [(4, 1), (3, 2), (2, 4), (1, 5)] 

lista = [5,17,32,12,15,62,237,244,76,21]
print(lista)
# [5, 17, 32, 12, 15, 62, 237, 244, 76, 21]
filtrirana_lista = list(filter(lambda x: (x % 5 == 0), lista))
print('brojevi deljivi sa pet su: ', filtrirana_lista)
# brojevi deljivi sa pet su:  [5, 15]

niz = ['python', 'PHP', 'js', 'Java', 'SQL', 'scala']
print(niz)
#['python', 'php', 'js', 'java', 'sql', 'scala']
filtrirana_lista = list(filter(lambda x: (x[0].lower() == 'p'), niz))
print('reci koje pocinju slovom P :' , filtrirana_lista)
#reci koje pocinju slovom P : ['python', 'PHP']
# x[0] prvo slovo

def kvadriraj(broj):
    return broj**2
print(kvadriraj(2))
# 4
lista = [1,2,3,4,5,6,7,8,9,10]
print(map(kvadriraj, lista))
# <map object at 0x0000029C66E87400>
nova_lista = list(map(kvadriraj, lista))
print(nova_lista)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lambda_lista = list(map(lambda broj: broj ** 2, lista))
print(lambda_lista)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

moja_lista = ['data analyst', 'data science', 'machine learning', 'ai']
mapirana_lista = list(map(lambda x: x[0].upper()+x[1:], moja_lista))
print(mapirana_lista)
# ['Data analyst', 'Data science', 'Machine learning', 'Ai']
# x[1:] pocinje od prvog karaktera i ide kroz celu listu-ne menja



######### bibliotelke ###########
from functools import reduce
#iz modula functools uvozimo alat reduce
lista = [1,2,3,4,5,6,7,8,9,10]
suma = reduce((lambda x, y: x + y), lista)
# 1+2=3 3+6=6 6+4....
print('suma elemenata liste je ', suma)
# suma elemenata liste je  55

lista = [110, 53, 3, 424, 255, 16, 42, 256]
najveci_broj = reduce((lambda x, y: x if (x>y) else y), lista)
print('najveci broj liste je: ', najveci_broj)
# najveci broj liste je:  424
#110 sa 53, 110 sa 3, 110 sa 424, 424 sa 255.... 

# ternarni operator x if (x>y) else y
starost = 18
poruka = 'punoletan(na) si ' if starost >= 18 else 'maloletan(na) si'
print(poruka)
#punoletan(na) si

lista = ['dragan', 'marko', 'jovan', 'milica', 'tamara', 'slobodan']
filtrirana_lista = list(filter(lambda x: (x[-1 ] == 'n'), lista))
print('imena koja zavrsavaju na slovo N su ', filtrirana_lista)
# imena koja zavrsavaju na slovo N su  ['dragan', 'jovan', 'slobodan']


