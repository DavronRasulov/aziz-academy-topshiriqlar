n = int(input())
sonlar = list(map(int, input().split()))

yigindi = 0 
for x in sonlar:
    yigindi += x
    
ortacha = yigindi / n

count = 0
for x in sonlar:
    if x > ortacha:
        count += 1
print(count)