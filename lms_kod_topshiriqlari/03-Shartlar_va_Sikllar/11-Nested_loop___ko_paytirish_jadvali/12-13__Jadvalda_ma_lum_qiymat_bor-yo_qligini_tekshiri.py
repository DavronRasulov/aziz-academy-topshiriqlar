a, b = map(int, input().split())
n = int(input())

if (a * b) % n == 0:
    print("Yes")
else:
    print("No")