yashirin_son = 6 
urinish = 3

i = 0 

while i < urinish:
    son = int(input())
    
    if son < 1 or son > 10:
        print("Invalid")
        continue
        
    i += 1 
    
    if son == yashirin_son:
        print("Correct")
        break
    else:
        print("Wrong")
else:
    print("Game Over")