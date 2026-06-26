n = int(input())
sonlar = list(map(int, input().split()))

musbat_yigindi = 0

for x in sonlar:
    if x > 0:
        musbat_yigindi += x 
        
print(musbat_yigindi)