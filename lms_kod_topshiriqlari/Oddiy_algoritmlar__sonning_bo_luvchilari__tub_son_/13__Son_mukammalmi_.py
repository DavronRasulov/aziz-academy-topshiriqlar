n = int(input())

if n <= 1:
    print("Not Perfect")
else:
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
            
    if s == n:
        print("Perfect")
    else:
        print("Not Perfect")