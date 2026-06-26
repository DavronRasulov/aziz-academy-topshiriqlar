n, m = map(int, input().split())

for i in range(1, n + 1):
    
    qator_sonlari = []
    for j in range(m):
        qator_sonlari.append(str(i))
        
    print(" ".join(qator_sonlari))