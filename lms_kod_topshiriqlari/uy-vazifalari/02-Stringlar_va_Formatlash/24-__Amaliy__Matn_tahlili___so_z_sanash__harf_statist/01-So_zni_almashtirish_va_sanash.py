matn = input()
soz = input()

boliklar = matn.split()
soni = 0 
natija = []

for b in boliklar:
    if b == soz:
        natija.append(b.upper())
        soni += 1 
    else:
        natija.append(b)
        
print(' '.join(natija))
print(soni)