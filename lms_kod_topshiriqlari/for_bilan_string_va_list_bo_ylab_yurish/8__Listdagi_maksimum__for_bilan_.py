n = int(input())
numbers = input().split()

max_num = int(numbers[0])

for num in numbers:
    num = int(num)
    if num > max_num:
        max_num = num
print(max_num)