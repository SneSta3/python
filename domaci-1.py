#Zadatak 1: Ispis svih elemenata liste
#Zadatak: Napišite program koji ispisuje sve elemente liste koristeći for petlju. Prvo napravite listu i onda izlistaje elemente, probajte jednu sa brojevima, a jednu npr sa stringovima.

vina = ['pjenusavo', 'bijelo', 'roze' , 'crveno', 'desertno']
print(vina)
vina = ['pjenusavo ', 'bijelo ', 'roze ' , 'crveno ', 'desertno ']
for vino in vina:
    print(vino)
# rezultat
    #pjenusavo
    #bijelo
    #roze
    #crveno
    #desertno

#Zadatak2: Kvadriranje brojeva u listi. 
# Zadatak: Napišite Python program koji prolazi kroz listu brojeva i kreira novu listu u kojoj su svi brojevi kvadrirani.  Evo i liste brojevi = [1, 2, 3, 4, 5] 

brojevi = [1, 2, 3, 4, 5] 
for broj in brojevi:
    print(broj**2)    
# rezultat 1 4 9 16 25

#Zadatak 3: Sabiranje svih brojeva u listi. 
# Napišite Python program koji sabira sve brojeve u listi. brojevi = [3, 7, 2, 9, 12] 

brojevi = [3, 7, 2, 9, 12] 
rezultat = 3 + 7 + 2 + 9 + 12
print(rezultat)
# rezultat 33

#Zadatak 4: Obrnuta lista Zadatak: 
# Napišite Python program koji obrće redosled elemenata u listi. lista = [1, 2, 3, 4, 5]

lista = [1, 2, 3, 4, 5]
print(lista[::-1])
# rezultat [5,4,3,2,1]

#Zadatak 5: Konkatenacija stringova u listi 
# Napišite Python program koji spaja (konkateniše) sve stringove u listi u jedan string. stringovi = ["Python", "je", "zabavan", "jezik"]

stringovi = ["Python", "je", "zabavan", "jezik"]
print(stringovi)
print("Python " + "je " + "zabavan " + "jezik")
# rezultat Python je zabavan jezik

#Zadatak 6: Proizvod svih brojeva u listi 
# Python program koji računa proizvod svih brojeva u listi. brojevi = [2, 3, 4, 5] (koristiti pelju npr)

brojevi = [2, 3, 4, 5]
print(2*3*4*5)
# rezultat 120 /////// ne znam ovo
# uz pomoc 
brojevi = [2, 3, 4, 5]
rezultat = 1
for broj in brojevi:
       rezultat *= broj
       print(rezultat)
# rezultat 
# 2
# 6
# 24
# 120    

#Zadatak 7: Provera da li broj postoji u listi. 
# Zadatak: Napišite Python program koji proverava da li zadati broj postoji u listi. brojevi = [10, 23, 5, 67, 42] Proverite da li npr 23 postoji u listi.

brojevi = [10, 23, 5, 67, 42]
print(23 in brojevi)
# rezultat True

#Zadatak 8: Ispis parnih brojeva iz liste 
# Napišite Python program koji prolazi kroz listu i ispisuje samo parne brojeve. brojevi = [12, 15, 7, 8, 20, 33] Ovaj zadnji je uslovno receno tezi za vas jer smo se samo dotakli petlji, ali ajd probajte.

brojevi = [12, 15, 7, 8, 20, 33]
parni_brojevi = [broj for broj in brojevi if broj % 2 == 0]
print(parni_brojevi)
# rezultat [12, 8, 20]






