file = open("Huzaifa.txt", "r")
print(file.read())
file.close()

print("\n Number of words in Huzaifa.txt are:")

with open("Huzaifa.txt", "r") as file1:
    data = file1.read()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)

print("\n Appending to the file Huzaifa.txt;")

file2 = open("Huzaifa.txt", "a")
file2.write("\n  I am appending this file because I want to. YOU HAVE A PROBLEM WITH THAT?!!!!!!!!!!!!!!!!")
file2.close()


with open("Condigal.txt", "r") as file3:
    data1 = file3.read()
with open("Ali.txt","r") as file3:
    data2 = file3.read()
data1 += "\n"
data1 += data2
print("Merging two files.....Condigal.txt and Ali.txt")
with open("MergedFile.txt", "w") as file4:
    file4.write(data1)
    print("Merged file created successfully")    
        





