n = int(input())

sonlar = list(map(int, input().split()))

min_qiymat = sonlar[0]

for son in sonlar:
    if son < min_qiymat:
        min_qiymat = son
        
print(min_qiymat)