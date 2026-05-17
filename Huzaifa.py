file = open("Huzaifa.txt", "r")
print(file.read())
file.close()


file1 = open("Huzaifa.txt", "a")
file1.write("\n  I am appending this file because I want to. YOU HAVE A PROBLEM WITH THAT?!!!!!!!!!!!!!!!!")
file1.close()


file2 =open('Huzaifa.txt', 'r')
print(file2.read())
file2.close()

file3 = open('Huzaifa.txt', 'w')
file3.write(" Hello I am Huzaifa.")
file3.close()