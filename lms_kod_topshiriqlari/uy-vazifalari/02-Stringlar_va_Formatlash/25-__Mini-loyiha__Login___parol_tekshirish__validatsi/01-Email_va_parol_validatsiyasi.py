email = input()
parol = input()

if ('@' in email) and ('.' in email) and (8 <= len(parol) <= 16) and (email == email.lower()):
    print(True)
else:
    print(False)