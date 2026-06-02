n = int(input())
sonlar = list(map(int, input().split()))

min_juft = None

for x in sonlar:
    if x % 2 == 0:
        if min_juft is None or x < min_juft:
            min_juft = x 
            
if min_juft is None:
    print("No")
else:
    print(min_juft)