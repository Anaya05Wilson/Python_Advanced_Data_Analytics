user_db={}
keys=[]
i=0
with open("student_db.csv","r") as f:
    data=f.readlines()
headers=data[0].strip().split(",")
user_db ={h: [] for h in headers}
for line in data[1:]:
    values=line.strip().split(",")
    for key, value in zip(headers,values):
        user_db[key].append(value)

def login(name):
    if name in user_db["name"]:
        password=input("Enter your password: ")
        if user_db["password"][user_db["name"].index(name)]==password:
            return True
        else:
            return False
    else:
        print("Name not found.")
        return False
    
name=input("Enter your name: ")
if user_db["status"][user_db["name"].index(name)]=="1":
    print("You are already logged in.")
else:
    if login(name):
        print("Login successful.")
        user_db["status"][user_db["name"].index(name)]="1"
    else:
        print("Login failed. Incorrect password.")