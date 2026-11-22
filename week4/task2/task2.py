balance = 50000
while True:
    print("1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        print("Balance:", balance)
    elif choice == '2':
        amt = float(input("Enter deposit amount: "))
        if amt <= 0:
            print("Invalid amount.")
        else:
            balance += amt
            print("New balance:", balance)
    elif choice == '3':
        amt = float(input("Enter withdrawal amount: "))
        if amt <= 0:
            print("Invalid amount.")
        elif amt > balance:
            print("Insufficient balance.")
        else:
            balance -= amt
            print("New balance:", balance)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")