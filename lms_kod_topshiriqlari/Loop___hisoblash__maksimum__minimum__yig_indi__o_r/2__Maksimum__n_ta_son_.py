n = int(input())

sonlar = list(map(int, input().split()))

max_qiymat = sonlar[0]

for son in sonlar:
    if son > max_qiymat:
        max_qiymat = son 

print(max_qiymat)