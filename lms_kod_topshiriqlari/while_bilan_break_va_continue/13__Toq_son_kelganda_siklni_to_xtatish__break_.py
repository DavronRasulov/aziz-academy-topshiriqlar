summa = 0

while True:
    n = int(input())
    
    if n % 2 != 0:
        break
    summa += n
    
print(summa)