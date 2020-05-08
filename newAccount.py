import random
import datetime

# First Action Prompt


# verifying in login details
def verifyUserLogin(username,password):
    loginSuccessful = []
    with open("staff.txt", "r") as user:
        allUsers = user.readlines()
        for users in allUsers:
            singleUserArray = users.split(',')
            #print(singleUserArray)
            if username == singleUserArray[0] and password == singleUserArray[1]:
                loginSuccessful.append(1)
                break
            else:
                loginSuccessful.clear()
    if(len(loginSuccessful) >= 1):
        print("Login Successful")
        return True
    else:
        print("Wrong Username or Password")
        return False
         

# saving account info and number to text file
def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Opening the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


# Generating Account number
def acct_number():
        accountNumber = ("30" + str(random.randint(10,99999999)))
        return accountNumber

# Creating new account information
def accounntInfo():
    accountName = input("Enter Account Name: ").title()
    openingBalance = input("Enter Opening Balance: ")
    accountType = input("Enter Account Type: ").title()
    accountEmail = input("Enter Email Address: ") 
    accountNumber = acct_number()
    accountDetails = accountNumber + ',' + accountName + ',' + openingBalance + ',' + accountType + ',' + accountEmail
    append_new_line('customer.txt',accountDetails)
    print("Your Account Number is: " + accountNumber)


# Read customer file for account Number Saved
def retrieveAccount(accountNumber):
    customerArray = []
    with open("customer.txt", "r") as user:
        allUsers = user.readlines()
        for users in allUsers:
            singleUserArray = users.split(',')
            #print(singleUserArray)
            if accountNumber == singleUserArray[0]:
                # fetching the user details from file
                customerArray.append(singleUserArray)
                break
            else:
                customerArray.clear()
    if(len(customerArray) >= 1):
        print(customerArray)
        return True
    else:
        print("Wrong Account Number")
        return False

def inside():
    print('''
            Please choose interest:
            1) Create New Bank Account
            2) Check Account Details
            3) Logout
            ''')
    interest = input("Choice: ").upper()
    if interest == "1":
        accounntInfo()
        inside()
        
    elif interest == "2":
        while True:
            accountRequest = input("Enter Account Number: ")
            re = retrieveAccount(accountRequest)
            if re:
                inside()

    elif interest == "3":
        ses = open('session.txt', 'r+')
        ses.truncate(0)
        ses.close()
        print("Logged Out...Thank You ")
        return
    else:
        print("Enter One the options Provided")


# requesting for login details
def BankApp():
    while True:
        print("""
A) Staff Login
B) Close App
    """)
        actions = input("Choice: ").upper()
        if actions == "A":
            while True:
                userName = input("Username: ").title()
                passWord = input("Password: ").title()
                verify = verifyUserLogin(userName,passWord)
                if verify:
                    # loginInfo = {"Username": userName, "Password": passWord}
                    x = str(datetime.datetime.now())
                    ses = open("session.txt", "a")
                    ses.write(x)
                    ses.close()
                    break
            inside()
            
        elif actions == "B":
            break
        else:
            print("Enter A or B")
        

BankApp() 




       
        
    
