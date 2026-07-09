name = input().strip()

formatted_name = " ".join(word.capitalize() for word in name.split())

print(formatted_name)
print(formatted_name[0])