n = int(input())

arr = list(map(int, input().split()))

for x in arr:
    if x % 5 == 0:
        print(x)