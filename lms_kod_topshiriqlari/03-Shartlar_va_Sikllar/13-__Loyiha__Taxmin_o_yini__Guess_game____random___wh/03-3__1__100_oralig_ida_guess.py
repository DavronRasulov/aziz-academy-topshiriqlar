yashirin_son = 42 

while True:
    try:
        qator = input()
        if not qator:
            break
            
        son = int(qator)

        if son < yashirin_son:
            print("Low")
        elif son > yashirin_son:
            print("High")
        else:
            print("Correct")
            
    except EOFError:
        break
    except ValueError:
        print("Iltimos, butun son kiriting!")
        