new = open("new.txt", "w")
new.close()

#check if the exist
import os
print("Checking if the file exist or not....")
if os.path.exists("new.txt"):
    print("The file exist")
else:
    print("The file does not exist")

    #creat a new if it does not exist
    myfile = open("myfile.txt", "w")
    myfile.write("Hi, I am Huzaifa ")
    myfile.close()

    #delete the file named Ali.txt if it exist
    os.remove("Ali.txt")


    #delete the folder
    os.rmdir("FolderName")
