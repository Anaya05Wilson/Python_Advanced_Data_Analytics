balance=10000
pin = 1234
print("Welcome to the ATM Machine\n")
while True:
    op= int(input("Choose an option: \n1. Withdraw \n2. Check Balance \n3. Exit\n"))
    if op == 1:
        amnt = int(input("Enter the amount to withdraw: "))
        if amnt > balance:
            print("Insufficient Balance")
            print("Thank you for using the ATM Machine. Goodbye!")
            break
        else:
            user_pin = int(input("Enter your PIN: "))
            if user_pin == pin:
                balance -= amnt
                print(f"Please collect your cash. Your remaining balance is {balance}")
                print("Thank you for using the ATM Machine. Goodbye!")
                break
            else:
                print("Incorrect PIN")
                break
    elif op == 2:
        print(f"Your current balance is {balance}")
        break
    else:
        print("Thank you for using the ATM Machine. Goodbye!")
        break
