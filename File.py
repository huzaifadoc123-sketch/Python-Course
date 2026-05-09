file = open("Condigal.txt", "r")

print(file.read())

file.close()


file_read = open("Condigal.txt", "r")
print("File in Read mode:-")
print(file_read.read())
file_read.close()

file_write = open("Condigal.txt", "w")
file_write.write("This is the new content of the file.")
file_write.write("Hi, I am a Penguin, I am a bird but I cannot fly.")
file_write.close()

file_append= open("Condigal.txt", "a")

file_append.write("\n file in append mode:-")
file_append.write("\n I am a Penguin, I am a bird but I cannot fly.")
file_append.close()