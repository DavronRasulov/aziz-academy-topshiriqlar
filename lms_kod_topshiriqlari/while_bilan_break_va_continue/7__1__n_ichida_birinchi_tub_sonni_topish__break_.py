n = int(input())

if n < 2:
    print("No")
else:
    i = 2 
    while i <= n:
        j = 2 
        tub = True
        
        while j < 1: 
            if i % j == 0:
                tub = False
                break
            j += 1
            
        if tub:
            print(i)
            break
            
        i += 1