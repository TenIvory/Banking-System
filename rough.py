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




