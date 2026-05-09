file= open("Condigal.txt","r")
counter = 0

Content = file.read()
#splittig content into lines
#and storing them in a list
Colist = Content.split("\n")

for i in Colist:
    if i:
        counter +=1
print("This is the number of lines in the file:") 
print(counter)       