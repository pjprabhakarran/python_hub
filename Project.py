# import JSON package
import json

# Regular Expression
import re

regex = '^[a-z0-9]\w{2,1000}[@]\w{4,1000}.com\Z$'
reg_pass = '[a-z][0-9][!@#$%^&*][A-Z]\w{4,16}'


# Validate Email Address
def chk(email):
    if re.search(regex, email):
        return "Valid"
    else:
        return "invalid"

# Validate Password
def chkpass(password):
    if not re.search('[A-Z]', password):
        print("- Password should contain at least 1 upper case character")
    if not re.search('[a-z]', password):
        print("- Password should contain at least 1 lower case character")
    if not re.search('[0-1]', password):
        print("- Password should contain at least 1 numeric value")
    if not re.search('[!@#$%^&*+]', password):
        print("- Password should contain at least 1 numeric value")
    if not 5 < len(password) < 17:
        print("- Password length should be 5 to 16 characters")
    else:
        return "Valid"

# Landing Page
print("Hello,Welcome to the Login Application!")
print("- Enter 1 To Register")
print("- Enter 2 To login if you are an existing user")
print("- Enter 3 To Reset password if forgotten")
x = int(input("Choose an option:"))

# User Creation if user chooses to register
if x == 1:
    with open('password.json') as json_file:
        data_js = json.load(json_file)

    val_catch = data_js
    json_file.close()
    name = input("Enter your Email:")
    if chk(name) == "Valid":
        password = input("Enter your Password:")
        if chkpass(password) == "Valid":
            temp = {name: password}
            val_catch.update(temp)
            with open('password.json', 'w') as json_file:
                json_file.write(json.dumps(val_catch))
            json_file.close()
            print("You have been successfully registered in the system")
    else:
        print("Enter a valid email address")


# Login module if an existing user wants to access
elif x == 2:
    print("Please Enter your credentials below:")
    with open('password.json') as json_file:
        dat = json.load(json_file)

    Dat_lookup = dat
    user = input("Enter your registered Email:")
    password = input("Enter your Password:")
    if user in Dat_lookup.keys():
        if password == Dat_lookup.get(user):
            print("Your have logged in successfully")
        else:
            print("Enter valid credentials")
    else:
        print("User not found, Kindly register in the system")

# Reset Password | Forget Password section
elif x == 3:
    with open('password.json') as json_file:
        dat = json.load(json_file)

    Dat_lookup = dat
    user = input("Enter your email to fetch password:")
    if user in Dat_lookup.keys():
        print(f'Please note down your password:{Dat_lookup.get(user)}')
    else:
        print("User not found, kindly register in the system")
else:
    print("Your input is invalid")
