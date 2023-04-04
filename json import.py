import json #imports json into the package

json.dump #takes the dictonaries you pass and dump  it into a file
json.load #retrives the data stored in dumps back into a dictionary

data = {"name":"Jack", "age":12} #creates a dictionary called data where name is mapped to jack and age is mapped to 12

with open("abc.json", "w") as f: #creates a json file called abc and write privlages are given
    json.dump(data, f) #dumps all the data from dictionary data into a file called f

with open("abc.json", "r") as f:
    print(json.load(f))
