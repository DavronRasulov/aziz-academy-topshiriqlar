yashirin_son = 4 
urinishlar = 3 

for i in range(1, urinishlar + 1):
    son = int(input())
    
    if son == yashirin_son:
        print(f"Correct in {i} tries")
        break
else:
    print("Game Over")