u = "admin"
p = "secret"
attempts = 3
while attempts > 0:
    user = input("Username: ")
    pwd = input("Password: ")
    if not user or not pwd:
        print("Empty username or password rejected.")
        continue
    if user == u and pwd == p:
        print("Login successful.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect. Attempts remaining:", attempts)
        else:
            print("Account locked.")