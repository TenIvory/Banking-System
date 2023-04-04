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

createAccount("John", "A234567!") #Creates a User named John    
createAccount("Johnny", "34567") #Will be asked to choose a new password



