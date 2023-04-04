import string
import hashlib
"""
f = open("abc.txt", "w")  # allows us to open any file we want, even if it doesn't exist.
# There are three levels, w = write, a = append, r = read. r will not work if the file doesn't exist. it will create
# a file and then work.; a and w will work even if file doesnt exist.
f.write("Hello world") #writes the message into the file abc.txt
f.close()  # close the file and allows us to manipulate it from somewhere else. If it is not closed, it remains open and
# cannot be used somewhere else

#another way to create a file is
with open("abc.txt", "a") as f: #the keyword 'with' will close the file automatically
    f.write("Good morning") #a is append and adds two messages together

with open("abc.txt", "r") as f: #r is read and reads and stores the data as strings which can be printed
    print(f.read())



print(string.ascii_letters) #prints all the letters in the string library
print(string.digits) #prints all the digits in string library
print(string.punctuation) #prints all punctuations in string library



def validate(password, charset): #validate method takes password and also a variable charset that stores ascii values from string library
    for i in password: #for every letter in the password given
        if i in charset: #if the word considered is present in the variable charset
            return True #then it will return true
    return False #if there are not even one instance of letters in password that is not present in charset variable it will return false


validate("ABCDE", "ABCDEFGH")
if (validate == True):
    print("exists")
else:
    print("Nope")

    """
password = "abcde"
hashed = hashlib.sha256(password.encode())
print(hashed.hexdigest())

def hashPassword(password):
    hashed = hashlib.sha256(password.encode())
    return hashed