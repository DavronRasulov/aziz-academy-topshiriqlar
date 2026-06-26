s = input()
new_s = ""

for char in s:
    if char == 'a':
        new_s += '@'
    else:
        new_s += char
        
print(new_s)