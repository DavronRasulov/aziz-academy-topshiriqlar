n = int(input())

yigindi = 0 
i = 1 

while i <= n:
    if i % 9 == 0:
        i += 1 
        continue
    yigindi += i 
    i += 1 
print(yigindi)