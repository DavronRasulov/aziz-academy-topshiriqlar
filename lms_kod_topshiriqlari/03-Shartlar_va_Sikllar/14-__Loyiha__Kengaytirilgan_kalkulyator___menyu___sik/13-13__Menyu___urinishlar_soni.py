count = 0

while True:
    data = input().split()
    
    if len(data) == 1 and data[0] == "0":
        print(count)
        break
        
    if len(data) == 2:
        a = int(data[0])
        b = int(data[1])
        continue
        
    tanlov = int(data[0])
    
    if 1 <= tanlov <= 6:
        count += 1
