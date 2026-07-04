height = 4 

for i in range(height):
    spaces = " " * (height - 1 - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
    
for _ in range(2):
    print(" " * (height - 1) + "|")