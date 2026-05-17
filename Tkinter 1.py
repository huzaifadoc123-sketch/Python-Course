from tkinter import *

window = Tk()
window.title("Tkinter Sample Window")
window.geometry("300x300")


greeting = Label(text=" Hello User", fg="black", bg="white")
button = Button(text="Click me", bg="black", fg="white")
entry = Entry(fg="yellow",bg="Blue",width=60)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
label = Label(master=frame, text="Sample frame")
label.pack()

textbox=Text(fg="green",bg="yellow")
textbox.pack()