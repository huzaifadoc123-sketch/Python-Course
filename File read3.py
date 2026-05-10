file1 = open("Safwan.txt", "r")
file2 = open("Huzaifa.txt", "w")

#reading each line from original text file
for line in file1.readlines():

    #reading all lines that do not begin with "class"
    if not (line.startswith("class")):
        print(line)


        #storing only those lines that do not begin with "class" in a new text file
        file2.write(line)

file2.close()
file1.close()        

    