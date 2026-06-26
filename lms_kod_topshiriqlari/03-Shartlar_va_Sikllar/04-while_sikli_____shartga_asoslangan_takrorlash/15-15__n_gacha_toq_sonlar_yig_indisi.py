n = int(input())

i = 1 
summa = 0

while i <= n:
    if i % 2 == 1:
        summa += i
    i += 1
print(summa)