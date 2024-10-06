x = 1
if x == True:
    print(True)

x = 0
if x == True:
    print(True)
else:
    print(False)

x = 100
y = 20    
if x < y:
    print('izraz je tacan,')
else:
    print('izraz je netacan') 

year = 2024 
if (year == 2024):
    print('trenutno je godina 2024')
else:
    print('trenutna godina nije 2024')

godisnji = False
if godisnji == True:
    print('uzivaj dok odmaras')
else:
    print('strpi se jos malo')

godisnji = True
if godisnji == True:
    print('uzivaj dok odmaras')
else:
    print('strpi se jos malo')

x = 9
if(x%2 == 0):
   print(' broj je paran')    
else:
    print('broj je neparan')

#dodatni uslovi elif
a = 2090
b = 2090
if a < b:
    print('a je manje od b')
elif a == b:
    print(' a i b su jednaki')
else:
    print('a je vece od b')

temperatura = 16
if temperatura > 30:
    print('sorc i papuce su resenje')
elif temperatura > 20:
    print('fino je napolju, moze kratka majica')
elif temperatura > 15:
    print('neki dobar duks')
else:
    print('ladnoca, obuci se dobro')

rezultat_testa = 50
if rezultat_testa > 90:
    print('odlican rezultat')
elif rezultat_testa >= 70 and rezultat_testa <=90:
    print('skroz dobar rezultat')    
elif rezultat_testa >= 50 and rezultat_testa <=70:
    print('prosao si ali moze bolje')  
else:
    print('pojma nemas')

########### while ###########

broj = 1
while broj <= 10:
    print(broj)
    broj += 1     #broj = broj + 1

limit = 10
counter = 1
while(counter < limit):
    print(counter)
    counter += 1
print(counter)

########## for ###############

brojevi = [1,2,3,4,5]
for broj in brojevi:
    print(broj * 2)

#print(1*2)
#print(2*2)
#print(3*2)
#print(4*2)
#print(5*2)

#print(brojevi)
#for i in range(1,6):
   # print(i)




    