import json


def writeData(data):  # creates a function writeData which takes data strings as parameters
    with open("data.json", "w") as f:  # opens and automatically closes the file data.json when done. has write privlage
        json.dump(data, f)  # dumps data into file f


def readData(
        data):  # reads the data from file f; Hwoever it'll throw an error if file doesnt exist which in this case it doesnt
    try:  # exception block. if there is a file data.json, it will read it and store the data to variable called data
        with open("data.json", "r") as f:
            data = json.load(f)
    except:  # if file doesnt exist then it catches the error and returns an empty dictionary
        data = {}  # shows an empty dictionary since there is nothing in the data.json file
    return data  # returns data if it is found.


#writeData({"user1": {"password": 123456, "balance": 0}}) #the first dictionary stores username details while second dictionary keeps balance and password of the user
def isPasswordValid(password):
    len(password) >= 8 and len(password) <= 16:

def createAccount(username, password):
    data = readData()
    if username not in data.keys():
        pass