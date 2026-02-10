balance = 10000
pin = 1234
pin_attempts = 3

print("Welcome to the ATM Machine\n")

while True:
    print("Choose an option:")
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    op = int(input("Enter your choice: "))

    if op == 1:
        amount = int(input("Enter the amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount. Please enter a valid amount.\n")
            continue

        if amount > balance:
            print("Insufficient Balance\n")
            continue

        attempts = 0
        while attempts < pin_attempts:
            user_pin = int(input("Enter your PIN: "))
            if user_pin == pin:
                balance -= amount
                print(f"Please collect your cash.")
                print(f"Remaining balance: {balance}\n")
                break
            else:
                attempts += 1
                print(f"Incorrect PIN. Attempts left: {pin_attempts - attempts}")

        if attempts == pin_attempts:
            print("Too many incorrect PIN attempts. Card blocked.\n")
            break

    elif op == 2:
        print(f"Your current balance is: {balance}\n")

    elif op == 3:
        print("Thank you for using the ATM Machine. Goodbye!")
        break

    else:
        print("Invalid option. Please choose again.\n")
