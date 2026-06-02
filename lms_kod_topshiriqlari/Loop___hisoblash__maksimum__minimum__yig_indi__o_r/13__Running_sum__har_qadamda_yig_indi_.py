n = int(input())

sonlar = []
while len(sonlar) < n:
    sonlar += list(map(int, input().split()))

yigindi = 0

for x in sonlar:
    yigindi += x
    print(yigindi)