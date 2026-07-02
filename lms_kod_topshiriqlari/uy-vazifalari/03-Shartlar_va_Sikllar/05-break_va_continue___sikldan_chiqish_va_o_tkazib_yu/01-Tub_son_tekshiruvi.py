n = int(input())

is_prime = True 

if n < 2:
    is_prime = False 
else:
    i = 2
    while i * i <= n: 
        if n % i == 0:
            is_prime = False
            break 
        i += 1 
        
if is_prime:
    print("ha")
else:
    print("yo'q")