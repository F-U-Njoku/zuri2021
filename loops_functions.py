import random
from datetime import datetime

allowedUsers = {'Seyi':["passwordSeyi",3383690575],'Mike':["passwordMike",9548447439], 'Love':["passwordLove",4399371430],}
options = {1:"Withdrawal", 2:"Cash Deposit", 3:"Complaint"}
inputs = {1:"How much would you like to withdraw?", 2:"How much would you like to deposit?", 3:"What issue will you like to report?"}
outputs = {1:"take your cash", 2:"NGN 2,000", 3:"Thank you for contacting us"} #Keeping a static balance for simplcity.

def bankOperations():
    print("These are the available options:")
    
    for key,value in options.items():
      print(f"{key}. {value}.")
    try:
      choice = int(input("Please select an option: "))
      request = input(inputs[choice])
      print(outputs[choice])
    except:
      print("Invalid option! Please try again!")
      

def login():
    name = input("What is your username? \n")
    if name in allowedUsers.keys():
        password = input("Your password? \n")
        if password == allowedUsers[name][0]:
            print(f"Welcome {name}!")
            print(datetime.now())
            
            bankOperations()
        else:
            print("Password incorrect, please try again!")
    else:
        print("Name not found, please try again!")

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password_verify = input("Enter password again: ")
    if (password != password_verify):
        print("Password does not match, please try again.")
    else:
        allowedUsers[username] = [password, random.randrange(10**9, 10**10)]
        print("Your account number is: " +str(allowedUsers[username][1]))
        login()
            
print("Welcome, have an account?")
print("1. Login")
print("2. Create an coount")

selection = int(input("Choose an option: "))

if (selection==1):
    login()
else:
    register()


  

