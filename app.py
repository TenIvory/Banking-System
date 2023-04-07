import json
import string #library allowing us to get all charcters, diigts and punctuations
import hashlib #library allowing us to start hashing passwords

def writeData(data): # function writeData takes data as parameter
    with open("data.json", "w") as f: #opens data.json file and has write privlages
        json.dump(data, f) #stores the data in a file f.


def readData():  # reads the data from file f; Hwoever it'll throw an error if file doesnt exist which in this case it doesnt
    try:  # exception block. if there is a file data.json, it will read it and store the data to variable called data
        with open("data.json", "r") as f:
            data = json.load(f)
    except:  # if file doesnt exist then it catches the error and returns an empty dictionary
        data = {}  # shows an empty dictionary since there is nothing in the data.json file
    return data  # returns data if it is found.

def writeTransactions(transaction): #a function to record all transactions done by different accounts
    with open("transactions.txt", "a") as f: #saves the transactions to a text file
        f.write(f"{transaction} /n") #permanently writes all transactions


#writeData({"user1": {"password": 123456, "balance": 0}}) #the first dictionary stores username details while second dictionary keeps balance and password of the user

def validate(password, charset): #validate method takes password and also a variable charset that stores ascii values from string library
    for i in password: #for every letter in the password given
        if i in charset: # even if one word considered is present in the variable charset
            return True #then it will return true
    return False #if there are not even one instance of letters in password that is not present in charset variable it will return false


def isPasswordValid (password):
    chars = string.ascii_letters #all the ascii letters from string library is stored as chars variable
    digits = string.digits #all the digits from string library is stored as digits variable
    specials = string.punctuation #all the puntation marks from string library is stored as specials variable
 
    if len(password) >= 8 and len(password) <= 16: #if the password length is 8 or more and 16 or less then
        if validate(password, chars): #uses the validate method defined above to check if the letters of password is present in variable chars
            if validate(password, digits): #uses the validate method defined above to check if the numbers of password is present in variable digits
                if validate(password, specials): #uses the validate method defined above to check if the puntuations of password is present in variable specials
                    return True #The password is accepted only if it has numbers, digits and special keys
    return False #returns a false if there is nothing present in the password that is present in the three variables and hence invalid password

                    
def hashPassword(password): #creates a function to hash the password 
    hashed = hashlib.sha256(password.encode()) #hashlib uses sha256 algorithm to hash the password and .encode() method return the encoded version of password and stores it variable called hashed
    return hashed.hexdigest() #retruns the hashed variable which stores the hashed value of the password                


def createAccount(username, password): #creates a method createAccount which takes username and password as parameters
    data = readData() #reads data and stores it in data variable
    if username not in data.keys(): #checks if the username is already there in the database or not. will proceed only if the account is new 
        #and not present in the database
        if isPasswordValid(password): #Checks if the password given is valid using the function isPasswordValid defined above
             data[username]= {"password" : hashPassword(password), "balance": 0} #creates a new account with the username and password is hashed using hashing function defined above and sets new balance to 0
             writeData(data) #updates the data to data.json file
             print("Account Created Successfully")
        else:
            print("Please enter a stronger password") 
    else:
        print("User already exists. Choose a new username")

#createAccount("John", "A234567!") #Creates a User named John    
#createAccount("Johnny", "34567") #Will be asked to choose a new password

def IsLoggedIn(username, password): #defines a function to see if user is logged in that takes username and password
    data = readData() #reads data from data.json and stores in data variable
    if username in data.keys(): #checks if the entered username is present in the keys (usernames) in data.json file
        if hashPassword(password) == data[username]["password"]: #password entered is converted into its encrypted form and checked if it matches the one stored in data.json
           return True #returns true if password from function and data.json for that user matches
        else:
           print("Password incorrect") #prints an error message
           return False #returns a fase
    else:
        print("Username not found") #returns an error message
        return False #returns a false

#print(IsLoggedIn("Jhn","234567!")) #prints an error saying user not found as user doesnt exist in data.json file

def showOptions(): #Creates a UI menu for user once he logs in 
    print("#################################")
    print("### Options ###") #Prints a UI of sort to show a menu
    print("#################################")
    print("1. Deposit")
    print("2. Withdraw") #Actions avaialble for his account
    print("3. Transfer")
    print("4. Check balance")
    print("5. Change password")
    print("6. Logout")
    choice = -1 #trigger variable to make sure one choice is entered 
    while choice not in [1,2,3,4,5,6]: #as long as the choice is not in this array
        try: #try condition
            choice = int(input("Please select an action for your account[1:6]: "))
        except:
            pass
    return choice #returns the users choice if it satisfies all conditions
    
def deposit(username, amount): #builds a function to deposit money into the account of username
    data = readData() #reads data.json file
    data[username]["balance"] += amount #adds the amount specified to the balance of username
    writeData(data) #writes the data to make it permnanent 
    writeTransactions(f"{amount} deposited by {username}") #creates a log of transaction in transaction file
    print("Amount deposited successfully") #success message
    print("Balance is: ", data[username]["balance"]) #shows updatd balance

def withdraw(username, amount): #builds a function to withdraw money from username account
    data = readData() #reads data.json file
    if data[username]["balance"] - amount >=0: #checks if the user has sufficient balance to make transactions
       data[username]["balance"] -= amount #deducts the amount from user's balance
       writeData(data) #writes data to make it permanent 
       writeTransactions(f"{amount} withdrawn by {username}") #writes log of withdrawn to transaction file
       print("Amount withdrawn successfully") #success message
    else:
        print("Insufficient balance") #error message
        print("Balance is: ", data[username]["balance"]) #shows updated balance

def transfer(sender, reciever, amount): #function to transfer money
    data = readData()
    if data[sender]["balance"] - amount >0: #checks if sender has sufficient balance
        data[sender]["balance"] -= amount #deducts account from sender
        data[reciever]["balance"] += amount #adds money to reciever
        writeData(data) #writes data to make it permanent 
        writeTransactions(f"{amount} transferred by {sender} to {reciever}") #log
        print("Amount transferred successfully")
        print("Balance is: ", data[sender]["balance"])
    else:
        print("Insufficient balance")

def checkBalance(username): #function to check balance
    data =readData()
    balance = data[username]["balance"]
    return balance

def changePassword(username, password): #function to change password
    data = readData()
    if isPasswordValid(password): #checks if new input password is valid according to the conditions we specified
        data[username]["password"] = hashPassword(password) #updates the new password
        writeData(data)
        print("Password changed successfully")
    else:
        print("Choose a stronger password") #fails if the new password is not according to rules



def showMenu():
    print("#################################")
    print("### Welcome to Banking server ###") #Prints a UI of sort to show a menu
    print("#################################")
    print("1. Login")
    print("2. Create account")
    print("3. Exit")
    
    choice = -1 #choice is initiated to -1. trigger variable. if no choice is given, then error message saying no choice given is printed

    while choice not in [1,2,3]: #while loop will run as long as the choice is not 1,2,3
        try: #try condition
            choice = int(input("Enter your choice [1:3]: ")) #takes user input and asks user to choose between 1 and 3. converts the input to int
        except: #except condition
            pass #makes the loop run again
        return choice

while True: #loop will run as long as the conidition defined is true 
    choice = showMenu() #the choice of the user is stored in variable choice
    if choice ==1:
          print("#################################")
          print("### 1. LOGIN                  ###") #Prints a UI of sort to show a menu
          print("#################################")
          username = input("Enter your username: ")
          password = input("Enter your password: ")
          
          if IsLoggedIn (username, password):
            while True: #shows the options menu as long as user doesnt press 6 to log out
                option = showOptions()

                if option == 1:
                    print("########################################")
                    print("###              Deposit             ###")
                    print("########################################")
                    amount = -1
                    while amount <= 0:
                        try:
                            amount = int(input("Enter The Deposit Amount : "))
                        except:
                            pass
                    deposit(username, amount) 

                elif option == 2:
                    print("########################################")
                    print("###              Withdraw            ###")
                    print("########################################")
                    amount = -1
                    while amount <= 0:
                        try:
                            amount = int(input("Enter The Withdraw Amount : "))
                        except:
                            pass
                    withdraw(username, amount) 

                elif option == 3:
                    print("########################################")
                    print("###              Transfer            ###")
                    print("########################################")
                    amount = -1
                    while amount <= 0:
                        try:
                            amount = int(input("Enter the amount to be transferred: "))
                        except:
                            pass
                    reciever = input("Enter the username of the reciever: ")
                    transfer(username, reciever, amount)

                elif option == 4:
                     print("########################################")
                     print("###              Check Balance       ###")
                     print("########################################")

                     print(f"Your balance is {checkBalance(username)}")

                elif option == 5:
                    print("########################################")
                    print("###              Change password     ###")
                    print("########################################")

                    password = input("Enter your new password: ")
                    changePassword(username, password)

                elif option == 6:
                    break
                  
    elif choice ==2:
          print("#################################")
          print("### 2. CREATE ACCOUNT         ###") #Prints a UI of sort to show a menu
          print("#################################")
          username = input("Enter your username: ")
          password = input("Enter your password: ")
          createAccount(username, password)
          print("Account created successfully")

    elif choice == 3:
        break



        









