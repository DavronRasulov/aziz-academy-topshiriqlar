n = int(input())
sonlar = list(map(int, input().split()))

max_toq = None
for x in sonlar:
    if x % 2 != 0:
        if max_toq is None or x > max_toq:
            max_toq = x
            
if max_toq is None:
    print("No")
else:
    print(max_toq)