n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    if x % 2 == 0 or x < 0:
        print(x)