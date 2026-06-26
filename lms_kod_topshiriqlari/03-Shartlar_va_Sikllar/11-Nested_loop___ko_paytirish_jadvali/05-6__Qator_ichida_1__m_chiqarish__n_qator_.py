n, m = map(int, input().split())

for i in range(n):
    
    qator = []
    for j in range(1, m + 1):
        qator.append(str(j))
        
    print(" ".join(qator))