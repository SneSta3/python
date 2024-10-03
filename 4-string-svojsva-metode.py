# len - duzina stringa
ime = 'Snjeza'
print(len(ime))
print(ime.upper())
print(ime.lower())
space = 'razmak        izmedju          reci'
print(space)
print(space.capitalize())

#svako prvo slovo veliko
word = 'ja sam neki STRING'
print(word)
rec_kao_title = word.title()
print(rec_kao_title)

#split
name = 'Predrag Miki Manojlovic'
print(name.split())

car = 'Renault clio, mali gradski auto, 74 konja, bela boja'
print(car.split(','))

# strip
#ukljanja prazan prostor ili specificne znakove
tekst ='           Pozdrav svima koliko vas ima        '
ociscen_tekst = tekst.strip()
print(ociscen_tekst)

text = '-----------------------python ekipo pozdrav---------'
clean_text = text.strip('-')
print(clean_text)

tekst = 'yyyyyyyyyyyyPythonyyyyyyyyyy'
clean = tekst.strip('y')
print(clean)

#replace
team_lead = 'sloba je nas novi team lead'
print(team_lead.replace('sloba','milan'))

#count
#broji koliko puta se deo stringa pojavljuje

zaposleni = 'sloba je nas prvi zaposleni ali je dojadio i Bogu i ljudima pa bi mogao sloba da se skloni'
print(zaposleni.count('sloba'))
print(zaposleni.count('a'))

#in
izbor ='php ili python ili pak java, pitanje je sad? Sta odabrati u 2024.'
print('python' in izbor)
print('PHP' in izbor)

#not in
print('python' not in izbor)

#join
words = ['ovo', ' cemo', ' da',' spojimo',' pomocu',' join',' metode']
spoji = ''.join(words)
print(spoji)
spoji = '-'.join(words)
print(spoji)

#isalnum
tekst = 'slobadobrouciidobioje10'
print(tekst.isalnum())
tekst = 'sloba dobro uci i dobio je 10'
print(tekst.isalnum())
tekst = 'slobadobrouciidobioje=10!'
print(tekst.isalnum())

#isalpha
tekst = 'slobajeopetdoboi10naispitu'
print(tekst.isalpha())
tekst = 'slobajeopetdoboidesetnaispitu'
print(tekst.isalpha())








