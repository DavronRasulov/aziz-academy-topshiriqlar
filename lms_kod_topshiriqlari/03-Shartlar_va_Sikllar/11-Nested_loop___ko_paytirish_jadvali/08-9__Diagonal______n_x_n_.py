n = int(input())

for i in range(n):
    qator = []
    
    for j in range(n):
        if i == j:
            qator.append("*")
        else:
            qator.append(".")
            
    print("".join(qator))