secret = 5
count = 0

while True:
    n = int(input())
    count += 1
    
    if n == secret: 
        break
        
print(count)