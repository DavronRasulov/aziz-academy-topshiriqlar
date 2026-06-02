while True:
    data = input().split()
    
    if len(data) == 1 and data[0] == "0":
        print("Exit")
        break
        
    if len(data) == 2:
        a = int(data[0])
        b = int(data[1])
        continue
        
    tanlov = int(data[0])
    
    if tanlov == 1:
        print(a + b)
        
    elif tanlov == 2:
        print(a - b)
        
    elif tanlov == 3:
        print(a * b)
        
    elif tanlov == 4:
        print(a / b if b != 0 else "Xato")