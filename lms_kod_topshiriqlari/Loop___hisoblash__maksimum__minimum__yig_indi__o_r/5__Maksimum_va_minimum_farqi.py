n = int(input())
sonlar = list(map(int, input().split()))

mx = sonlar[0]
mn = sonlar[0]

for x in sonlar:
    if x > mx:
        mx = x
    if x < mn:
        mn = x
        
natija = mx - mn

print(natija)