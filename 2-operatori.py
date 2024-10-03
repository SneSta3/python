############# operatori #############
# vrste
    # aritmeticki
    # operatori dodele
    # operatori poredjenja
    # logicki operatori
    # bitovni operatori

#### aritmeticki operatori ####

#sabiranje
print(100 + 300)      
a = 100
b = 20
c = a + b
print(c)

a = 'BMW'
b = 10
# b = '10'
# print(a + ' ' + b)
print (a + ' ' + str(b))

#oduzimanje
a = 20
b = 5
c = a - b            
print(c)

#mnozenje
a = 10
b = 10
c = a * b
print(c)

a = 'snjeza'
b = 10
c = a * b
print(c)

#deljenje
a = 30
b = 6
c = a / b  #rezultat float
c = a // b #celobrojno deljenje
print(c) 

#modulo-ostatak pri deljenju
a = 20
b = 7
c = a % b
print(c)

#eksponent-stepenovanje
print(5**2)  #dize na kvadrat
print(5**3)  #diye na treci

########## redosled operacija ##########
print(1 + 4 * 2 + 3 -1)
print(1 + (4 * 2) + 3 -1)
print((2 + 2) *10)

########### operatori dodele ############
a = 30       #operator dodele
print(a)     #a=30

a += 20      #sabiranje i dodela  a=a+20
print(a)     #a=50
b =10
b += 20      #b=10+20
print (b)

a -= 20      #oduzimanje i dodela a=a-20
print(a)     #a=30
c = 100
c -= 70      #c=100-70
print (c)

d = 25       #deljenje i dodela   
d /= 5       #d=25/5
print(d)
e = 25       #celobrojno deljenje i dodela   
e //= 5      #e=25/5
print(e)

f = 3        #stepenovanje i dodela
f **= 2      #f=3**2
print (f)

########### operatori poredjenja ############
print('PYTHON' == 'python')  #False
print('Python' == 'python')  #False
print('python' == 'python')  #True

#==jednako je
x = 10
y = 10
print(x == y)       
print(10 == 10.0)  

#!=nije jednako
print(20 != 30)     

#> vece >= vece ili jednako
print(10 > 3)
print(10 >= 10)

#< manje <= manje ili jednako
print(10 < 3)
print(10 <= 10)

print(5 + 5 >= 3 + 3)

########### logicki operatori ############
# and = uslov je tacan ako su oba izraza True
print(2 < 10 and 20 > 5)
print(10 > 20 and 10 > 2)
# or = uslov je tacan ako je jedan od izraza True
x = 2
print(x == 2 or x == 100)
# not = reverse od True je False
x = 100
z = 100
print(not(x == y))
print(not(100 > 5))























