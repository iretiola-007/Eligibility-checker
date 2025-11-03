print("Welcome to loops!")

n = int(input("How many loops? "))
i = 0
while i < n:
    i += 1
    print(f"Looped {i} time{'s' if i> 1 else ''}")

