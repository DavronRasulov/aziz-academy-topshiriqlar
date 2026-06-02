n = int(input())
sonlar = list(map(int, input().split()))

min_qiymat = sonlar[0]
min_index = 0

for i in range(len(sonlar)):
    if sonlar[i] < min_qiymat:
        min_qiymat = sonlar[i]
        min_index = i
        
print(min_index)