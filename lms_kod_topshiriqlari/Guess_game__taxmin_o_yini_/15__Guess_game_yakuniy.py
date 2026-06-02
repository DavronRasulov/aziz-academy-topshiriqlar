yashirin_son = 20
urinishlar = 0

while True:
    son = int(input())
    urinishlar += 1
    
    if son < 1 or son > 20:
        print("Invalid")
        continue
        
    if son < yashirin_son:
        print("Low")
    elif son > yashirin_son:
        print("High")
    else:
        print("Correct")
        break
    
print(urinishlar)
    
