kunlar = int(input())
narx = int(input())
soliq_foizi = int(input())

yalpi = kunlar * narx 
soliq = yalpi * soliq_foizi // 100 
sof = yalpi - soliq

print(yalpi)
print(soliq)
print(sof)