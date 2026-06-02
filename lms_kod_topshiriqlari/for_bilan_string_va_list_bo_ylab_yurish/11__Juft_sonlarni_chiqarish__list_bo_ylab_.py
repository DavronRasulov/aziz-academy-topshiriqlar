n = int(input())
numbers = input().split()

for num in numbers:
    num = int(num)
    if num % 2 == 0:
        print(num)