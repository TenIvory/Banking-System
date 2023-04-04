def validate(password, charset): #validate method takes password and also a variable charset that stores ascii values from string library
    for i in password: #for every letter in the password given
        if i in charset: # even if one word considered is present in the variable charset
            return True #then it will return true
    return False #if there are not even one instance of letters in password that is not present in charset variable it will return false


testString = "112233A"
charset = "ABCDEFGHI"

if(validate(testString, charset)== True):
    print("Yes")
else:
    print("Nope")

