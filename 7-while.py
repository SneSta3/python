a = 1
while a < 10:
    print(a)
    a = a + 1 # a += 1
    #1 2 3 4 5 6 7 8 9 10

b = 1   
while b < 5:
    print(f'trenutna vrednost b je : {b}')
    b += 1
# trenutna vrednost b je : 1
#trenutna vrednost b je : 2
#trenutna vrednost b je : 3
#trenutna vrednost b je : 4

lista = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1
    # 1 2 3 4 5....

telefoni = ('iphone', 'samsung', 'nokia', 'honor', 'huawei')
i = 0
while i < len(telefoni):
    print(telefoni[i])
    i = i + 1
#iphone
#samsung
##nokia
#honor
#huawei

i = 5
while i < 10:
    i = i + 1
    if i == 7:
        continue
    print(i, end='')
    # 68910

brojac = 0
while brojac < 5:
    print('trenutna vrednost brojaca:', brojac)
    brojac += 1
else:
    print('petlja je zavrsena,konacna vrednost je ', brojac)
#renutna vrednost brojaca: 0
#trenutna vrednost brojaca: 1
#trenutna vrednost brojaca: 2
#trenutna vrednost brojaca: 3
#trenutna vrednost brojaca: 4
#petlja je zavrsena,konacna vrednost je  5

brojac = 0
while True:
    print('trenutna vrednost brojaca je :', brojac)
    brojac += 1
    if brojac == 5:
        break
#trenutna vrednost brojaca je : 0
#trenutna vrednost brojaca je : 1
#trenutna vrednost brojaca je : 2
#trenutna vrednost brojaca je : 3
#trenutna vrednost brojaca je : 4

brojac = 0
while brojac < 10:
    brojac += 1
    if brojac % 2 == 0:
        continue
    print(brojac)
    #1 3 5 7 9
    

