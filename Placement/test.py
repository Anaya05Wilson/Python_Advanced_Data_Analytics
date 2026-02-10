user_db = {}

try:
    with open("student_db.csv", "r") as f:
        data = f.readlines()
    headers = data[0].strip().split(",")
    user_db = {h: [] for h in headers}  
    for line in data[1:]:
        values = line.strip().split(",")
        for key, value in zip(headers, values):
            user_db[key].append(value)
    
    print("User Database:")
    print(user_db)
    print()
    
    name = input("Enter your name: ")
    if name in user_db["name"]:
        index = user_db["name"].index(name)      
        if user_db["status"][index] == "1":
            print("User already active.")
            print("Name:", user_db["name"][index])
            print("Status: Active")
        else:
            password = input("Enter your password: ")
            if user_db["pass"][index] == password:
                print("Login successful.")             
                user_db["status"][index] = "1"

                with open("student_db.csv", "w") as f:
                    f.write(",".join(headers) + "\n")
                    for i in range(len(user_db["name"])):
                        row = []
                        for h in headers:
                            row.append(user_db[h][i])
                        f.write(",".join(row) + "\n")

                print("Status updated to Active.")
                print("User Details:")
                print("Name:", user_db["name"][index])
                print("Status: Active")
            else:
                print("Invalid password.")
    else:
        print("User not present in database.")
except FileNotFoundError:
    print("Error: student_db.csv file not found.")
except Exception as e:
    print("Unexpected error:", e)
