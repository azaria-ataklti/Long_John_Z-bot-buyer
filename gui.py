from tkinter import *
print("Shoe name should replace spaces with dashes '-'")

#Main function that runs arguments to get link
def URLGen(name, model, size):
    BaseSize = 570
    # Base Size is for Shoe Size 6.5
    ShoeSize = size - 6
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'http://www.adidas.com/us/' + str(name) + "/" + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(
        ShoeSizeCode)
    return URL


# Use this as a flag to indicate if the box was clicked.

global clicked
global sizeClicked
global nameClicked

clicked = False
sizeClicked = False
nameClicked = False

#Default text functions
def callback(event):
    global clicked
    if (clicked == False):
        modelNumber.delete(0, END)         #
        modelNumber.config(fg = "black")   # Change the colour of the text here.
        clicked = True
def sizeCallback(event):
    global sizeClicked
    if (sizeClicked == False):
        size.delete(0, END)
        size.config(fg="black")
        sizeClicked = True
def nameCallback(event):
    global nameClicked
    if (nameClicked == False):
        name.delete(0, END)
        name.config(fg="black")
        nameClicked = True

master = Tk()
master.title("Long John Zilver")
var = StringVar()
modelNumber = Entry(master)
size = Entry(master)
name = Entry(master)


modelNumber.config(fg = "gray")
modelNumber.bind("<Button-1>", callback)
modelNumber.insert(0, "Model Number")

size.config(fg = "gray")
size.bind("<Button-1>", sizeCallback)
size.insert(0, "Size")

name.config(fg = "gray")
name.bind("<Button-1>", nameCallback)
name.insert(0, "Shoe Name")


modelNumber.pack()
size.pack()
name.pack()


modelNumber.focus_set()

if size.get() == "":
    print("Bad")

#Function to display URL after clicking button
def dispURL():
    w = Label(master, textvariable=var, relief=RAISED)
    var.set(URLGen(name.get(), modelNumber.get(), int(size.get())))
    w.pack()


b = Button(master, text = "Get your link!", width = 10, command= lambda: dispURL())
b.pack()

mainloop()


