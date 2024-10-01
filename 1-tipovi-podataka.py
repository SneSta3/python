# tipovi podataka ####################################

#  name             type
# integers          int      brojevi 3,9,90   
# floating points   float    decimalne vrednosti 3,14
# strings           str      uredjena sekvenca operatora 'tekst'
# booleans          bool     logicke vrednosti True i False
# lists             list     uredjena sekvenca objekata kada zelimo  da skladistimo vise varijabli ['snjeza', 'milica', 3.14, True]
# dictionaries      dict     neuredjena lista key value parova
# tuples            tup      uredjena imutabilna sekvenca objekata
# sets              set      neuredjena kolekcija unique vrednosti 


# da li je sve u pythonu objekat- DA
broj = 4
print (type(broj))
broj = 'cetiri'
print (type(broj))
print(type('snjeza'))  #type() ispitivanje tipa vrednosti

a = str('python')
print(type(a))
b = str('30')
print(type(b))
c = int('30')
print(type(c))
print(c)


# integers ########################################
a = 5
b = 100
c = 1000
print(c)
print(a + b +c)

a = 5
b = str(100)
c = 1000
print(type(b))
print(a + int(b) +c)

print(20/5) # 4.0
print(20//5) # 4

#float ###########################################
print(type(20/5))
pi = 3.14
print(type(pi))
x = int(3.9)
print(type(x))
print(x)

#complex ########################################
x = 2 + 3j
print(x)
print(type(x))

#strings ########################################
a = 'string'
b = "STRING"
c ='''DOCSSTRING'''
print(type(a))
d = str(300)
print(type(d))

#konkatenacija-spajanje teksta ##################
print('Hello ' + ' World')
ime = 'Jovan'
prezime = 'Jovanovic'
print(ime + ' ' + prezime)
puno_ime = ime + ' ' + prezime
print(puno_ime)

#join() #########################################
delovi_imena = ['Nikola', 'Tesla']
puno_ime = ' '.join(delovi_imena)
print(puno_ime)

delovi_imena = ['Jovan', 'Jovanovic', 'Zmaj']
puno_ime = ' - '.join(delovi_imena)
print(puno_ime)

#f string ######################################
ime = 'Snjeza'
godine = 41
opis = f'Moje ime je {ime} i imam {godine} godina'
print(opis)

#format ########################################
name = 'Snjeza'
age = '41'
message = 'Cao ja sam {} i imam {} godina'.format(name,age)
print(message)

podaci = {'ime':'Snjeza', 'grad':'Novi Sad' }
poruka = 'Stanijem u {grad} i zovem se {ime}'.format(**podaci)
print(poruka)

#list ###########################################
numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers))

moja_lista = []
# moja_lista.append(1)
# moja_lista.append(2)
# moja_lista.append(3)
print(moja_lista)

lista = [3.14, True, False, 100, ['x', 'y', 'z']]
print(lista)

laptops = ['dell lattitude', 'lenovo think pad', 'macbook pro']
#                 0                  1                 2
print('Ja od ovih modela koristim u kancelariji ' + laptops [1] + 'a na terenu i kuci ' + laptops[2])

brojevi = [1,2,3,5,8]
#          0 1 2 3 4   
# menja na odredjenu poziciju
brojevi[3] = 4
brojevi[4] = 5
brojevi.append(6)
# append dodaje na kraj liste
print(brojevi)
dodatni_brojevi = [7,8,9,10]
brojevi.extend(dodatni_brojevi)
# extend dodaje niz
brojevi.insert(9, 1000)
# dodaje na odredjenu poziciju
print(brojevi)

brojevi.remove(1000)
print(brojevi)
brojevi.append(10)
print(brojevi)
brojevi.remove(10)
print(brojevi)
# dve iste vrednosti,brise prvu vrednost

brojevi = [1,2,3]
poslednji = brojevi.pop()
print(brojevi)
print(poslednji)
# pop ukljanja poslednju vrednost ali ne brise

brojevi.clear()
print(brojevi)

brojevi = [ 100,200,300]
print(200 in brojevi) #True
print(2000 in brojevi) #False

# dictionaries #######################################
# svaki key je jedinstven
kursevi = {}
print(type(kursevi))
kursevi = {'kurs': 'python data analyst', 'predavac': 'slobodan miric'}
print(kursevi)
print(kursevi['kurs'])
print(kursevi['predavac'])

zaposleni = {
    'ime': 'snjezana',
    'godine': '41',
    'grad': 'novi sad'
}
print(zaposleni)

primer = dict(ime='snjeza', godine='41', grad='beograd')
print(primer)
#dict radi samo ako su kljucevi (ime,godine...) stringovi bez razmaka,da je jedna rec, bez brojeva, bez specijalnih karaktera

primer2 = {1: 'jedan', 2:'dva', 3:'tri'}  
print(primer2)
# ugnjezden recnik
zaposleni = {
    '1':{'ime':'snjeza', 'pozicija':'web designer'},
    '2':{'ime':'sloba', 'pozicija': 'predavac'}
}
print(zaposleni)
print(zaposleni['1']['ime'])
print(zaposleni['2']['pozicija'])

#tuples ##############################################
#neizmenjiva lista elemenata -torke
kurs = ('python data anlyst', 3, 'meseca')
print(kurs)
print(type(kurs))
print(kurs[0] +  ' kurs traje '  + str(kurs[1])  + ' ' + kurs [2])

brojevi = (1,2,3,4,5)
print(brojevi[0])
# brojevi[0] = 2000
# brojevi.append(400)
print(brojevi)

#sets ###############################################
#unikatni elementi, nema odredjeni redosled, moze da se menja ali nema duplikata
rokovi = {'decembar', 'jun', 'septembar', 'jun', 'decembar'}
print(type(rokovi))
print(rokovi)

brojevi = {1,2,3}
brojevi.add(4)
print(brojevi)
brojevi.remove(4)
print(brojevi)

neparni = {1,3,5,7,9}
parni = {2,4,6,8,10}
unija =neparni.union(parni)
print(unija)

#booleans ############################################
print(True)
print(False)

#dinamic typing
ljubimac = 100
ljubimac = ['pas', 'Frida']
print(ljubimac)





















