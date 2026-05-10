file_read = open("Condigal.txt", "r")
print("File in Read mode:")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open("Condigal.txt", "w")
print("File in Write mode:")
file_write.write("Helllllllllllllllllooooooooooooooooooooooooooooo")
file_write.close()

#open the file in append mode
file_append = open("Condigal.txt", "a")
print("File in Append mode:")
file_append.write("\nWho are you! First tell me who are you!No you first!No, you first!. Nah Forget it")
file_append.close()