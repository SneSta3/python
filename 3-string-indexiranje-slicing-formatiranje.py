print('ja sam string')
print("i ja sam string")

print("I'm ukulele player and I also played the harmonica")
print("I\"m ukulele player and I also played the harmonica")

guitar = 'fender stratocaster'
print(guitar)

car = 'renault clio'
#      01234567891011  index  
auto = 'r   e  n   a  u    l  t'
#       0  -6 -5  -4  -3  -2 -1
print(car[3])  #index-[]
print(auto[-1])

############# slicing ################
#    string[start: stop: step]
kurs = 'python kurs'
# osnovni slicing
print(kurs[0:6:1])
print(kurs[0:6:2]) #step 2-svako drugo slovo
print(kurs[7:11])  #kurs
print(kurs[7:])    #kurs

#slicing bez starta i stopa
print(kurs[:7])  #[0:7:1] python
print(kurs[4:])  #on kurs
print(kurs[:])   #[sve] python kurs

#korak u slicingu
print(kurs [::2])  #svaki drugi pto us

#obrnuti slicing
print(kurs[::-1])  #sruk nohtyp

#negativni indexi
print(kurs[-1:])  #s
print(kurs[-4:])  #kurs
print(kurs[-12:]) #python kurs

print(kurs[12:6:-1])  #sruk
print(kurs[-1:-5:-1]) #sruk

brojevi = list(range(0,11))
print(brojevi)
print(brojevi[0:11:2])
print(brojevi[0:11:3])

#injektovanje varijable u string
user = 'snjeza'
print('dobrodosao ' + user + ' na nasu aplikaciju')

#string interpolacija
print('snjeza ima {} godina' .format(41))
print('{0} {2} {1}' .format('setanje psa','aktivnost','je moja glavna'))

print('{s} ima hobi i to su {t} i {c}' .format(t ='trening', c ='citanje', s='snjeza'))

ljubimac = 'freeda'
starost = 4
print(f"Moj ljubimac je pas {ljubimac} i ima {starost} godine")
















