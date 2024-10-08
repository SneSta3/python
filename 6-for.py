# for <varijabla> in <niz>
    # <blok koda>

for i in range(8):
    print(i) # 0,1,2,3,4,5,6,7

for i in range(1,6):
    print(i) #1,2,3,4,5

for i in range(1,11,2):
    print(i)    #1,3,5,7,9

brojevi = list(range(0,10))
print(brojevi) #[0,1,2,3,4,5,6,7,8,9]

x = []
for i in range(1,6):
    y = i ** 2
    x.append(y)
print(x) #[1,4,9,16,25]
print(max(x))  #25
print(min(x))  #1

brojevi = [1,2,3,4,5,6,7,8,9,10]
for broj in brojevi:
    print(broj)
    #1
    #2
    #3....
print('----------------------')    

for broj in brojevi:
    print(broj * 3)
    #3
    #6
    #9...
print('----------------------')    

for broj in brojevi:
    print(broj + 3)
    #4
    #5
    #6...

for x in brojevi:
    if x%2 == 0:
        print(f'ispis parnog proja:{x}')
       
    else:  
        print(f'ispis neparnog proja:{x}') 
       #ispis parnog proja:4
       #ispis neparnog proja:5

lista = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for broj in lista:
    suma = suma + broj
print(suma)  # 55

string = 'Python je fantastican jezik za programiranje'
for i in string:
    print(i)
    #p
    #a
    #j
    #t....
string = 'Python je fantastican jezik za programiranje'
for i in string:
    print(i, end='')    
#Python je fantastican jezik za programiranje


band = ['lars', 'james', 'kirk', 'robert']
for member in band:
    print(f'{member.title()}, je clan benda Metallica')
#Lars, je clan benda Metallica
#James, je clan benda Metallica
#Kirk, je clan benda Metallica
#Robert, je clan benda Metallica

niz = [1,2,3,4,5,6,7,8,9,10]
broj = 5
for i in niz:
    if i == broj:
        print('broj je pronadjen')
        break # kada nadje uslov, prekida izvrsavanje
else:
    print('broj nije pronadjen')
     #broj je pronadjen

for broj in range(10):
    if broj % 2 == 0:
        continue #preskoci uslov
    print(broj)         #1 3 5 7 9

for broj in [2,4,6,8,10]:
    if broj % 3 == 0:
        print(f'broj {broj} je deljiv sa 3')
        break
else:
    print('nema broja deljivog sa 3')    
    #broj 6 je deljiv sa 3

for broj in [2,4,6,8,10,12,15]:
    if broj % 3 == 0:
        print(f'broj {broj} je deljiv sa 3')
        break
else:
    print('nema broja deljivog sa 3')  
    #broj 6 je deljiv sa 3

#predavac = {
    #'boban' : 'html i css',
    #'danijel': 'javascript',
   # 'jovana': 'rect',
   # 'sloba': 'python',
   # 'milan': 'machine',
   # 'milica': 'data analyst',
   # 'sloba z': 'django'
#}    
#for predavac in predavaci:
   # print(predavac)

