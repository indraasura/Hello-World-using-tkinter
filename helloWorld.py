from tkinter import *
#Tk() is a constructor method assigned to variable root
#Creates a new top-level widget which will be the main level for app
root = Tk()
Label (root, text = "Hello World!").pack()
#.pack method displays the text in the window/GUI
#Label is a child of the root window
#.pack() is called a geometry management method

#now create loop to keep the window running so that we can see the text 
root.mainloop()
