n = int(input())
numbers = input().split()

min_num = int(numbers[0])

for num in numbers:
    num = int(num)
    if num < min_num:
        min_num = num 
        
print(min_num)