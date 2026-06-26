data = input().split()
n = int(data[0])
m = int(data[1])

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(".", end="")
    print()