name=input("Enter your name: ")
year=int(input("Enter your year of birth: "))
def print_name(name, year):
    if year<2000:
        print(f"{name}!!! Your birth year starts with 19ssss??? OMG!! You are too old")
    else:
        print(f"{name}. Your are too younggg")
print_name(name, year)