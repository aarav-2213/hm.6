

y = input("Enter character: ")

if len(y) > 1:
    print("\nWrite only 1 character to check")
else:
    if ('a' <= x <= 'z') or ('A' <= x <= 'Z'):
        print(x + " is alphabet.")
    else:
        print(x + " is not alphabet.")
