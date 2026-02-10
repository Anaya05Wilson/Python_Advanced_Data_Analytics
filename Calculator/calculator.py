#CALCULATOR

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

while True:
    print("#############")
    print("Calculator")
    print("#############")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    option = input("Choose an option (1,2,3,4,5): ")
    if option == '5':
        print("Exiting...")
        break
    if option in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if option == '1':
            print("Result: ", add(num1, num2))
        elif option == '2':
            print("Result: ", sub(num1, num2))
        elif option == '3':
            print("Result: ", mul(num1, num2))
        elif option == '4':
            print("Result: ", div(num1, num2))
    else:
        print("Invalid Input")

