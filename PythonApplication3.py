# Ülesanne 1 - while
nimi = input("Palun sisesta oma nimi: ")
kordi = int(input("Mitu korda tervitada? "))

nr = 1
while nr <= kordi:
    print("Oled tervitatud,", nimi + ",", nr, ". korda.")
    nr = nr + 1

# Ülesanne 1 - for
nimi = input("Palun sisesta oma nimi: ")
kordi = int(input("Mitu korda tervitada? "))

for i in range(1, kordi + 1):
    print("Oled tervitatud,", nimi + ",", i, ". korda.")

# Ülesanne 2 - while (lõpetamine Enteriga)
summa = 0

while True:
    sisend = input("Sisesta arv (lõpetamiseks vajuta Enter): ")
    if sisend == "":
        break
    arv = int(sisend)
    summa = summa + arv

print("Sisestatud arvude summa on", summa)

# Ülesanne 2 - for (lõpetamine Enteriga)
summa = 0

for i in range(1000):
    sisend = input("Sisesta arv (lõpetamiseks vajuta Enter): ")
    if sisend == "":
        break
    arv = int(sisend)
    summa = summa + arv

print("Sisestatud arvude summa on", summa)

# Ülesanne 3 - while
import random

õige = 0
kord = 0

while kord < 10:
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    vastus = int(input(f"Mis on {a} + {b}? "))
    if vastus == a + b:
        print("Õige! Väga tubli!")
        õige = õige + 1
    else:
        print("Vale! Õige vastus oli", a + b)
    kord = kord + 1

print("Sul oli", õige, "õiget vastust 10-st.")

# Ülesanne 3 - for
import random

õige = 0

for i in range(10):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    vastus = int(input(f"Mis on {a} + {b}? "))
    if vastus == a + b:
        print("Õige! Tubli!")
        õige = õige + 1
    else:
        print("Vale, õige vastus oli", a + b)

print("Kokku õigeid vastuseid:", õige, "/ 10")

# Ülesanne 3 - while (5 katset iga tehte jaoks)
import random

õige = 0
kord = 0

while kord < 10:
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    õige_vastus = a + b
    katse = 0
    vastatud = False

    while katse < 5:
        vastus = int(input(f"Mis on {a} + {b}? "))
        if vastus == õige_vastus:
            print("Õige! Väga hea!")
            õige = õige + 1
            vastatud = True
            break
        else:
            print("Vale! Proovi uuesti.")
        katse = katse + 1

    if not vastatud:
        print("Kaotasid! Õige vastus oli", õige_vastus)
    kord = kord + 1

print("Sul oli", õige, "õiget vastust 10-st.")

# Ülesanne 3 - for (5 katset iga tehte jaoks)
import random

õige = 0

for i in range(10):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    õige_vastus = a + b
    vastatud = False

    for j in range(5):
        vastus = int(input(f"Mis on {a} + {b}? "))
        if vastus == õige_vastus:
            print("Õige! Väga tubli!")
            õige = õige + 1
            vastatud = True
            break
        else:
            print("Vale, proovi uuesti.")
    
    if not vastatud:
        print("Kaotasid! Õige vastus oli", õige_vastus)

print("Kokku õigeid vastuseid:", õige, "/ 10")

# Ülesanne 4 - while (korrutustabel)
a = 1

while a <= 10:
    b = 1
    while b <= 10:
        print(a, "x", b, "=", a * b)
        b = b + 1
    print()
    a = a + 1

# Ülesanne 4 - for (korrutustabel)
for a in range(1, 11):
    for b in range(1, 11):
        print(a, "x", b, "=", a * b)
    print()

# Ülesanne 5 - while, diagonaalid X
N = int(input("Sisesta ruudu suurus N: "))
rida = 0

while rida < N:
    veerg = 0
    while veerg < N:
        if veerg == rida or veerg == N - 1 - rida:
            print("X", end=" ")
        else:
            print("O", end=" ")
        veerg = veerg + 1
    print()
    rida = rida + 1

 # Ülesanne 5 - for, diagonaalid X
N = int(input("Sisesta ruudu suurus N: "))

for rida in range(N):
    for veerg in range(N):
        if veerg == rida or veerg == N - 1 - rida:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

# Ülesanne 6 - while, 5x5 tärnid
rida = 0

while rida < 5:
    veerg = 0
    while veerg < 5:
        print("*", end=" ")
        veerg = veerg + 1
    print()
    rida = rida + 1

# Ülesanne 6 - for, 5x5 tärnid
for rida in range(5):
    for veerg in range(5):
        print("*", end=" ")
    print()

# Kasvav kolmnurk - while
rida = 1

while rida <= 5:
    print("*" * rida)
    rida = rida + 1

# Kasvav kolmnurk - for
for rida in range(1, 6):
    print("*" * rida)

# Kahanev kolmnurk - while
rida = 5

while rida > 0:
    print("*" * rida)
    rida = rida - 1

# Kahanev kolmnurk - for
for rida in range(5, 0, -1):
    print("*" * rida)

# Ülesanne 7 - while
import random

loendur = 0
while loendur < 5:
    print(random.randint(0, 9), end="")
    loendur = loendur + 1
print()

# Ülesanne 7 - for
import random

for i in range(5):
    print(random.randint(0, 9), end="")
print()

# Ülesanne 8 - while
arv = 1
paaris = 0
paaritu = 0

while arv <= 100:
    if arv % 2 == 0:
        print(arv, "on paaris")
        paaris = paaris + 1
    else:
        print(arv, "on paaritu")
        paaritu = paaritu + 1
    arv = arv + 1

print("Paarisarve kokku:", paaris)
print("Paarituid arve kokku:", paaritu)

# Ülesanne 8 - for
paaris = 0
paaritu = 0

for arv in range(1, 101):
    if arv % 2 == 0:
        print(arv, "on paaris")
        paaris = paaris + 1
    else:
        print(arv, "on paaritu")
        paaritu = paaritu + 1

print("Paarisarve kokku:", paaris)
print("Paarituid arve kokku:", paaritu)

# Ülesanne 9 - while
i = 1
number = 5

while i <= 10:
    print(number, "x", i, "=", number * i)
    i = i + 1

# Ülesanne 9 - for
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Ülesanne 10 - while
arv = 1

while arv <= 100:
    if arv % 5 == 0:
        print(arv)
    arv = arv + 1

# Ülesanne 10 - for
for arv in range(1, 101):
    if arv % 5 == 0:
        print(arv)

# Ülesanne 11 - while
import random

while True:
    number = random.randint(1, 10)
    katse = 0
    arvas = False

    while katse < 3:
        vastus = int(input("Arva arv (1-10): "))
        if vastus == number:
            print("Õnnitleme! Arvasid õigesti!")
            arvas = True
            break
        else:
            print("Vale, proovi uuesti.")
        katse = katse + 1

    if not arvas:
        print("Kahjuks ei arvanud. Õige arv oli", number)

    uuesti = input("Kas soovid uuesti proovida? (jah/ei): ")
    if uuesti.lower() != "jah":
        break

# Ülesanne 11 - for
import random

while True:
    number = random.randint(1, 10)
    arvas = False

    for katse in range(3):
        vastus = int(input("Arva arv (1-10): "))
        if vastus == number:
            print("Õnnitleme! Arvasid õigesti!")
            arvas = True
            break
        else:
            print("Vale, proovi uuesti.")

    if not arvas:
        print("Kahjuks ei arvanud. Õige arv oli", number)

    uuesti = input("Kas soovid uuesti proovida? (jah/ei): ")
    if uuesti.lower() != "jah":
        break

# Ülesanne 12 - while
alg_summa = float(input("Sisesta summa, mida pangas hoida: "))
aastad = int(input("Mitu aastat raha hoida? "))
intress_protsent = 5

summa = alg_summa
aasta = 1

print("{:<6} {:<12} {:<10} {:<12}".format("Aasta", "Algsumma", "Intress", "Aasta lõpuks"))

while aasta <= aastad:
    intress = summa * intress_protsent / 100
    lopp_summa = summa + intress
    print("{:<6} {:<12.2f} {:<10.2f} {:<12.2f}".format(aasta, summa, intress, lopp_summa))
    summa = lopp_summa
    aasta = aasta + 1

kasum = summa - alg_summa
print("Summa kokku: {:.2f}€".format(summa))
print("Kasum: {:.2f}€".format(kasum))

# Ülesanne 12 - for
alg_summa = float(input("Sisesta summa, mida pangas hoida: "))
aastad = int(input("Mitu aastat raha hoida? "))
intress_protsent = 5

summa = alg_summa

print("{:<6} {:<12} {:<10} {:<12}".format("Aasta", "Algsumma", "Intress", "Aasta lõpuks"))

for aasta in range(1, aastad + 1):
    intress = summa * intress_protsent / 100
    lopp_summa = summa + intress
    print("{:<6} {:<12.2f} {:<10.2f} {:<12.2f}".format(aasta, summa, intress, lopp_summa))
    summa = lopp_summa

kasum = summa - alg_summa
print("Summa kokku: {:.2f}€".format(summa))
print("Kasum: {:.2f}€".format(kasum))

# Ülesanne 13 - while
arv = 1

print("{:<4} {:<6} {:<5}".format("Arv", "Ruut", "Kuup"))

while arv <= 10:
    ruut = arv * arv
    kuup = arv * arv * arv
    print("{:<4} {:<6} {:<5}".format(arv, ruut, kuup))
    arv = arv + 1

# Ülesanne 13 - for
print("{:<4} {:<6} {:<5}".format("Arv", "Ruut", "Kuup"))

for arv in range(1, 11):
    ruut = arv * arv
    kuup = arv * arv * arv
    print("{:<4} {:<6} {:<5}".format(arv, ruut, kuup))

# Ülesanne 14 - while
rida = 1

while rida <= 10:
    veerg = 1
    while veerg <= 10:
        print("{:>4}".format(rida * veerg), end="")
        veerg = veerg + 1
    print()
    rida = rida + 1

# Ülesanne 14 - for
for rida in range(1, 11):
    for veerg in range(1, 11):
        print("{:>4}".format(rida * veerg), end="")
    print()

# Ülesanne 15 - while
katse = 0

while True:
    vastus = input("Osta elevant ära! ")
    katse = katse + 1
    if vastus.lower() == "elevant":
        break

print("Küsimust esitati", katse, "korda.")

# Ülesanne 15 - for
katse = 0

for i in range(10):
    vastus = input("Osta elevant ära! ")
    katse = katse + 1
    if vastus.lower() == "elevant":
        break

print("Küsimust esitati", katse, "korda.")

# Ülesanne 16 - while
import random

min_arv = int(input("Sisesta vahemiku algus: "))
max_arv = int(input("Sisesta vahemiku lõpp: "))

number = random.randint(min_arv, max_arv)

while True:
    vastus = input("Arva arv või kirjuta 'lõpp' lõpetamiseks: ")
    if vastus.lower() == "lõpp":
        print("Mäng lõpetatud. Õige arv oli:", number)
        break
    if vastus.isdigit():
        if int(vastus) == number:
            print("Õige! Tubli!")
            number = random.randint(min_arv, max_arv)
        elif int(vastus) < number:
            print("Lihtsam!")
        else:
            print("Raskem!")
    else:
        print("Palun sisesta arv või 'lõpp'.")

# Ülesanne 16 - for
import random

min_arv = int(input("Sisesta vahemiku algus: "))
max_arv = int(input("Sisesta vahemiku lõpp: "))

number = random.randint(min_arv, max_arv)

for i in range(10):
    vastus = input("Arva arv või kirjuta 'lõpp' lõpetamiseks: ")
    if vastus.lower() == "lõpp":
        print("Mäng lõpetatud. Õige arv oli:", number)
        break
    if vastus.isdigit():
        if int(vastus) == number:
            print("Õige! Tubli!")
            number = random.randint(min_arv, max_arv)
        elif int(vastus) < number:
            print("Lihtsam!")
        else:
            print("Raskem!")
    else:
        print("Palun sisesta arv või 'lõpp'.")

# Ülesanne 17 - Turtle ruudustik
import turtle

horisontaalsed = int(input("Sisesta ruutude arv horisontaalsuunas: "))
vertikaalsed = int(input("Sisesta ruutude arv vertikaalsuunas: "))
ruudu_suurus = 50

# Kilpkonna seadistus
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-horisontaalsed * ruudu_suurus / 2, vertikaalsed * ruudu_suurus / 2)
t.pendown()

for rida in range(vertikaalsed):
    for veerg in range(horisontaalsed):
        for _ in range(4):
            t.forward(ruudu_suurus)
            t.right(90)
        t.penup()
        t.forward(ruudu_suurus)
        t.pendown()
    t.penup()
    t.goto(-horisontaalsed * ruudu_suurus / 2, vertikaalsed * ruudu_suurus / 2 - (rida + 1) * ruudu_suurus)
    t.pendown()

turtle.done()

# Ülesanne 18 - while
import random

loendur = 0
while loendur < 1:
    N = random.randint(1, 10)
    M = random.randint(1, 10)
    print("N:", N, "ruut:", N**2, "kuup:", N**3, "| M:", M, "ruut:", M**2, "kuup:", M**3)
    loendur = loendur + 1

# Ülesanne 18 - for
import random

for _ in range(1):
    N = random.randint(1, 10)
    M = random.randint(1, 10)
    print("N:", N, "ruut:", N**2, "kuup:", N**3, "| M:", M, "ruut:", M**2, "kuup:", M**3)

# Ülesanne 19 - while
import math

n = int(input("Mitu arvu soovid sisestada? "))

summa = 0
korrutis = 1
loendur = 0

while loendur < n:
    arv = float(input("Sisesta arv: "))
    summa = summa + arv
    korrutis = korrutis * arv
    loendur = loendur + 1

arit_keskmine = summa / n
geo_keskmine = korrutis**(1/n)

print("Summa:", summa)
print("Aritmeetiline keskmine:", arit_keskmine)
print("Geomeetriline keskmine:", geo_keskmine)
print("Korrutis:", korrutis)

# Ülesanne 19 - for
import math

n = int(input("Mitu arvu soovid sisestada? "))

summa = 0
korrutis = 1

for i in range(n):
    arv = float(input("Sisesta arv: "))
    summa = summa + arv
    korrutis = korrutis * arv

arit_keskmine = summa / n
geo_keskmine = korrutis**(1/n)

print("Summa:", summa)
print("Aritmeetiline keskmine:", arit_keskmine)
print("Geomeetriline keskmine:", geo_keskmine)
print("Korrutis:", korrutis)

# Ülesanne 20 - while
arv = input("Sisesta neliarvuline arv: ")

while len(arv) != 4 or not arv.isdigit():
    arv = input("Palun sisesta täpselt neliarvuline arv: ")

numbrid = [int(x) for x in arv]

suurim = max(numbrid)
vaikseim = min(numbrid)

print("Suurim number:", suurim)
print("Väikseim number:", vaikseim)

# Ülesanne 20 - for
arv = input("Sisesta neliarvuline arv: ")

while len(arv) != 4 or not arv.isdigit():
    arv = input("Palun sisesta täpselt neliarvuline arv: ")

numbrid = []
for x in arv:
    numbrid.append(int(x))

suurim = max(numbrid)
vaikseim = min(numbrid)

print("Suurim number:", suurim)
print("Väikseim number:", vaikseim)

# Ülesanne 21 - while
n = int(input("Mitu nime soovid sisestada? "))

nimed = []
loendur = 0

while loendur < n:
    nimi = input("Sisesta nimi: ")
    nimed.append(nimi)
    loendur = loendur + 1

pikim = max(nimed, key=len)
luhim = min(nimed, key=len)

print("Pikim nimi:", pikim)
print("Lühim nimi:", luhim)

# Ülesanne 21 - for
n = int(input("Mitu nime soovid sisestada? "))

nimed = []

for i in range(n):
    nimi = input("Sisesta nimi: ")
    nimed.append(nimi)

pikim = max(nimed, key=len)
luhim = min(nimed, key=len)

print("Pikim nimi:", pikim)
print("Lühim nimi:", luhim)

# Ülesanne 22 - while
katse = 0

while True:
    vastus = input("Tahan kommi! ")
    katse = katse + 1
    if vastus.lower() == "komm":
        break

print("Küsimust esitati", katse, "korda.")

# Ülesanne 22 - for
katse = 0

for i in range(10):
    vastus = input("Tahan kommi! ")
    katse = katse + 1
    if vastus.lower() == "komm":
        break

print("Küsimust esitati", katse, "korda.")

# Ülesanne 23 - while
n = int(input("Mitu õpilast küsida? "))

täisealised = 0
alaealised = 0
loendur = 0

while loendur < n:
    vanus = int(input("Sisesta õpilase vanus: "))
    if vanus >= 18:
        täisealised += 1
    else:
        alaealised += 1
    loendur += 1

print("Täisealised:", täisealised)
print("Alaealised:", alaealised)

# Ülesanne 23 - for
n = int(input("Mitu õpilast küsida? "))

täisealised = 0
alaealised = 0

for i in range(n):
    vanus = int(input("Sisesta õpilase vanus: "))
    if vanus >= 18:
        täisealised += 1
    else:
        alaealised += 1

print("Täisealised:", täisealised)
print("Alaealised:", alaealised)

def netopalk(bruto):
    maksuvaba = 170
    tulumaks_protsent = 20
    if bruto <= maksuvaba:
        neto = bruto
    else:
        tulumaks = (bruto - maksuvaba) * tulumaks_protsent / 100
        neto = bruto - tulumaks
    return round(neto, 2)

isa_bruto = float(input("Sisesta isa brutopalk: "))
ema_bruto = float(input("Sisesta ema brutopalk: "))
lapsed = int(input("Sisesta alaealiste laste arv: "))

isa_neto = netopalk(isa_bruto)
ema_neto = netopalk(ema_bruto)

toetus = lapsed * 50

pere_sissetulek = isa_neto + ema_neto + toetus

print("Pere kuusissetulek:", round(pere_sissetulek, 2), "€")

# Ülesanne 24
import re

registreerimisnumber = input("Sisesta auto registreerimisnumber: ").upper()

pattern = r"^[0-9]{3}[A-Z]{3}$"

if re.match(pattern, registreerimisnumber):
    print("On Eesti registreerimisnumber")
else:
    print("Ei ole Eesti registreerimisnumber")