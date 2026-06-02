yashirin_son = 8
max_urinishlar = 3

for i in range(max_urinishlar):
    try:
        qator = input()
        if not qator:
            break
            
        son = int(qator)
        
        if son == yashirin_son:
            exit()

    except (EOFError, Valuerror):
            break

else:
    print("Game Over")