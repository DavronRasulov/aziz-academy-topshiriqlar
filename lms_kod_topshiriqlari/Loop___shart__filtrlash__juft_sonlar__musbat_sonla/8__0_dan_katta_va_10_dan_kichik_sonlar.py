n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    if 0 < x < 10:
        print(x)