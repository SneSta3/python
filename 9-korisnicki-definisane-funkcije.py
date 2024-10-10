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


