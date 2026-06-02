n = int(input())
sonlar = list(map(int, input().split()))

max_qiymat = sonlar[0]
max_index = 0

for i in range(len(sonlar)):
    if sonlar[i] > max_qiymat:
        max_qiymat = sonlar[i]
        max_index = i
        
print(max_index)