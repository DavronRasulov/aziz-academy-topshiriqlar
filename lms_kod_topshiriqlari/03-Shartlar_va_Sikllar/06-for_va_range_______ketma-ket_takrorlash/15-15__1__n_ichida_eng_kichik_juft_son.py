n = int(input())

min_juft = None

for i in range(1, n + 1):
    if i % 2 == 0:
        min_juft = i
        break
        
if min_juft is None:
    print("No")
else:
    print(min_juft)
