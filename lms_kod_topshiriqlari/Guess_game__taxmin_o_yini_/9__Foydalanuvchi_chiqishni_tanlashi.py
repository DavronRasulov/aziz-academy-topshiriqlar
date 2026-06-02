son = int(input())

if son == 0:
    print("Exit")
else:
    yashirin_son = 3
    while True:
        if son == yashirin_son:
            print("Correct")
            break
        else:
            print("Wrong")
            
        son = int(input())
        
        if son == 0:
            print("Exit")
            break