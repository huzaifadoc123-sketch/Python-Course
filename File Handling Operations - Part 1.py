with open("Alii.txt","w") as file:
    file.write("Hi! I am Alii.")
    file.close()

    #split file into words
    with open("Alii.txt","r") as file:
        data = file.read()
        print("Words in this file are...")
        for line in data:
            word = line.split()
            print(word)
    file.close()        