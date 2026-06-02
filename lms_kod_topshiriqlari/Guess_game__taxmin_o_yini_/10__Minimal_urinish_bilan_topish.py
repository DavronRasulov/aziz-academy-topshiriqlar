yashirin_son = 1 
urinishlar = 0

while True:
    son = int(input())
    urinishlar += 1
    
    if son == yashirin_son:
        print("Correct")
        break
    else:
        print("Try again")
        
print(urinishlar)