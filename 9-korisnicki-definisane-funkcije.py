def moja_funkcija():
    print('pozdrav iz funkcije')
moja_funkcija()
   #pozdrav iz funkcije

def sabiranje(broj1,broj2): #parametri
    return broj1 + broj2
rezultat = sabiranje(10, 30) #argumenti/vrednosti
print(rezultat)

#def povrsina_kruga(r):
    #povrsina = 3.14 * r * r
    #print(povrsina)
#povrsina_kruga(2) 
#povrsina = povrsina_kruga(2)
#print(povrsina)

def povrsina_kruga(r):
    povrsina = 3.14 * r * r
    return povrsina
povrsina = povrsina_kruga(4)
print(povrsina) 
# 50.24

def podeli(a, b):
    if b == 0:
        print('nije dozvoljeno deljenje sa nulom')
        return
    rezultat = a / b
    return rezultat 
print(podeli (100,5)) # 20
print(podeli (100,0)) # nije dozvoljeno deljenje sa nulom
                      # none

#lokalne promenjljive/varijable-dostupne samo unutar funkcije

def lokalne_varijable():
    x = 100   #promenjljiva definisana unutar funkcije
    print(x)
lokalne_varijable()     #100
#print(x)  #Error: name 'x' is not defined

#globalne promenjive
y = 29
def globalne_varijable():
    print(y)
globalne_varijable()
# 29    

z = 20
def moja_funkcija ():
    z = 60
moja_funkcija()
print(z) #20

z = 20
def moja_funkcija ():
    global z
    z = 60
moja_funkcija()
print(z) #60

def amelova_f():
    print(z)
amelova_f()  #60

z = 100
def amelova_f():
    print(z)
amelova_f()  #100

def uporedi(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print('brojevi su jednaki')
print(uporedi(10,3))        # 10
print(uporedi(10,30))       # 30
print(uporedi(30,30))       # brojevi su jednaki
                            #None

def uporedi(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print('brojevi su jednaki')
        return x
print(uporedi(30,30))  # brojevi su jednaki
                       # 30

def odakle_si(drzava):
    print('moja rodna gruda je ' + drzava)
odakle_si ('hrvatska')                           
odakle_si ('srbija')  
odakle_si ('bih')  
# moja rodna gruda je hrvatska
# moja rodna gruda je srbija
# moja rodna gruda je bih
#odakle_si()
# Error: odakle_si() missing 1 required positional argument: 'drzava'

def odakle_si(drzava ='njemacka'):
    print('moja rodna gruda je ' + drzava)
odakle_si('hrvatska')                           
odakle_si('srbija')  
odakle_si('bih')
odakle_si()
# moja rodna gruda je njemacka

def puno_ime(ime, prezime):
    print(ime + ' ' + prezime)
puno_ime('amel', 'omanovic') 
puno_ime('sandra', 'cirkovic') 
puno_ime('svetlana', 'stojnovic')
# amel omanovic
# sandra cirkovic
# svetlana stojnovic

def porodica(*clan):
    print('danas su na redu za usisavanje ' + clan[0] + ' i ' + clan[3])
porodica('tamara', 'jovana', 'mirka', 'dragica')
# danas su na redu za usisavanje tamara i dragica





