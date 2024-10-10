import math
# def 

def pozdrav(ime):
    print(f'zdravo, {ime}')
pozdrav('amele') 
pozdrav('snezo')    
pozdrav('marko')  
#zdravo, amele
#zdravo, snezo
#zdravo, marko

#ime = input('unesite vase ime')
#print('dobrodosli', ime)
#unesite vase ime _____
#unesite vase ime snjeza
#dobrodosli snjeza

#godina_rodjenja = int(input('unesite godinu rodjenja'))
#trenutna_godina = 2024
#godine = trenutna_godina - godina_rodjenja
#print('imate', godine, 'godina')
#unesite godinu rodjenja1983
#imate 41 godina

python = 'zdravo svete'
print(len(python)) #12
print(python.upper()) #metoda/vezana za objekat ili klasu .znaci da je vezano/upper je vezano za stringove
#ZDRAVO SVETE

lista = [1,2,3,4,5]
print(type(lista))
lista.append(6)
print(lista)
# [1, 2, 3, 4, 5, 6]
lista.pop()
print(lista)
#[1, 2, 3, 4, 5]

brojevi = [1,2,3,4]
ukloni_broj = brojevi.pop(1)
print(brojevi)
#[1, 3, 4]
print(ukloni_broj)
#2

brojevi = [1,2,3,4,]
del brojevi[1]
print(brojevi)
#[1, 3, 4]
brojevi = [1,2,3,4,]
del brojevi[1:3]
print(brojevi)
#[1, 4]

brojevi = [1,2,3,2,4]
brojevi.remove(2)
print(brojevi)
#[1, 3, 2, 4]

# new_list = [expresion for item in itrerable if condition]
numbers = [1,2,3,4,5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)
#[1, 4, 9, 16, 25]

matrica = [[1,2,3],
           [4,5,6],
           [7,8,9]]

#for red in matrica:
    #for element in red:
       # print(element, end=' ') #1 2 3 4 5 6 7 8 9
   # print() #123
             #456
             #789

# new_list = [expresion for item in itrerable if condition]
spajanje = [num for row in matrica for num in row]
print(spajanje)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

brojevi = [1,2,3,4,5]
brojevi = [x for x in brojevi if x %2 != 0]
print(brojevi)
#[1, 3, 5]

brojevi = [1,2,3,4,5]
neparni_brojevi = []
for x in brojevi:
    if x% 2 != 0:
        neparni_brojevi.append(x)
print(neparni_brojevi)        
#[1, 3, 5]

niz = [10,20,30,40,50]
print(min(niz)) #10
print(max(niz)) #50

stringovi = ['tamara', 'marko', 'jovana','slobodan']
print(min(stringovi)) #jovana
print(max(stringovi)) #tamara

#array = ['sneza', 40, True, 'python']
#print(max(array))

x = round(9.876543)
print(x) #10
x = round(9.876543,1) #9.9
x = round(9.876543,2) #9.88
print(x)


#import math
broj = 7.9
zaokruzi_nadole = math.floor(broj)
print(zaokruzi_nadole) #7
zaokruzi_nagore = math.ceil(broj)
print(zaokruzi_nagore) #8

mojtupl = (1,2,3,4,5,6,7,8,9,10)
print(mojtupl) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
zbroji = sum(mojtupl)
print(zbroji) #55

mojalista = [1,2,3,4,5,6,7,8,9,10]
saberi = sum(mojalista)
print(saberi) #55

lista = [2, 4, 1.34, 4/3, 3.14, 2, 18.99]
suma = sum(lista)
print(suma)
#32.803333333333335
lista = [2, 4, 1.34, 4/3, 3.14, 2, 18.99]
suma = sum(lista)
suma = round(sum(lista),3)
print(suma) #32.803

x = pow(2,3)
print(x) #8

lista = [10, 67, 270 ,149, 14]
print(sorted(lista))
#[10, 14, 67, 149, 270]
print(lista)
#[10, 67, 270, 149, 14]

nova_lista = sorted(lista)
print(nova_lista)
#[10, 14, 67, 149, 270]

obrni_listu = sorted(nova_lista, reverse=True)
print(obrni_listu)
#[270, 149, 67, 14, 10]

#rezultat = input('unesi ime:')
#print('dobrodosao ' + rezultat + ' na python data analyst kurs')
#unesi ime:_______
##unesi ime:snjeza
#dobrodosao snjeza na python data analyst kurs
#print(type(rezultat))

from random import shuffle
lista = [1,2,3,4,5,6,7,8,9,10]
shuffle(lista)
print(lista)
#[10, 6, 5, 8, 4, 2, 1, 3, 7, 9]
#[7, 8, 2, 6, 5, 1, 4, 10, 9, 3]

voce = ['banana', 'jagoda', 'ananas','jabika','sljiva','visnja']
shuffle(voce)
print(voce)
#['banana', 'visnja', 'ananas', 'jagoda', 'sljiva', 'jabika']
#['visnja', 'jagoda', 'banana', 'sljiva', 'ananas', 'jabika']

from random import randint
broj = randint(0,100)
print(broj)
#10
#26 ....

from random import choice
smuti = ['banana', 'jabuka','kruska','malina','sojino mleko', 'jogurt']
element = choice(smuti)
print(element)
#kruska
#sojino mleko










