from tkinter import *
from teaFunctionality import *
class aGUI:
    def __init__(self, master): #just the gui for now
        self.master = master
        self.teaFunctionality = teaFunctionality()
        master.title("A simple GUI")

        # base entry box
        self.baseEntry = Entry(master)
        self.baseEntry.insert(0, "enter tea base")
        self.baseEntry.pack()

        # sugar entry box
        self.sugarEntry = Entry(master)
        self.sugarEntry.insert(0, "enter sugar amount")
        self.sugarEntry.pack()

        # size entry box
        self.sizeEntry = Entry(master)
        self.sizeEntry.insert(0, "enter size")
        self.sizeEntry.pack()

        # not sure how to handle toppings

        # milk button
        self.milkButton = Button(master)
        self.milkButton["text"] = "got milk",
        self.milkButton["command"] = self.teaFunctionality.milkPressed
        self.milkButton.pack({"side": "left"})

        # hot button
        self.hotButton = Button(master)
        self.hotButton["text"] = "hot",
        self.hotButton["command"] = self.teaFunctionality.hotPressed
        self.hotButton.pack({"side": "left"})

        # cold button
        self.coldButton = Button(master)
        self.coldButton["text"] = "cold",
        self.coldButton["command"] = self.teaFunctionality.coldPressed
        self.coldButton.pack({"side": "left"})

        # warm button
        self.warmButton = Button(master)
        self.warmButton["text"] = "warm",
        self.warmButton["command"] = self.teaFunctionality.warmPressed
        self.warmButton.pack({"side": "left"})

        # should print out the tea from the given entries and buttons
        self.getTeaButton = Button(master)
        self.getTeaButton["text"] = "What tea have I made?"
        self.getTeaButton["command"] = self.teaFunctionality.generatePressed
        self.getTeaButton.pack({"side": "left"})

        # text box where the print goes
        self.textBox = Text(self, height=2, width=10)
        self.textBox.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


root = Tk()
my_gui = aGUI(root)
root.mainloop()





'''



class aGUI:
    
    def __init__(self, master): #just the gui for now
        self.master = master
        master.title("TEAAAAAAAAAA")

        self.baseEntry = Entry(self)
        self.baseEntry.insert(0, "enter tea base")
        self.baseEntry.pack({"side": "left"})
        
        #base entry
        self.baseEntry = Entry(self)
        

        #sugar entry box
        self.sugarEntry = Entry(self)
        self.sugarEntry = Entry(1, "enter sugar amount")
        self.sugarEntry.pack({"side": "left"})

        #size entry box
        self.sizeEntry = tkinter.Entry()
        self.sizeEntry = tkinter.Entry(2, "enter size")
        self.sizeEntry.pack({"side": "left"})

        #not sure how to handle toppings

        #milk button
        self.milkButton = tkinter.Button(self)
        self.milkButton["text"] = "got milk",
        self.milkButton["command"] = self.teaFunctionality.milkPressed
        self.milkButton.pack({"side": "left"})

        #hot button
        self.hotButton = tkinter.Button(self)
        self.hotButton["text"] = "hot",
        self.hotButton["command"] = self.teaFunctionality.hotPressed
        self.hotButton.pack({"side": "left"})

        #cold button
        self.coldButton = tkinter.Button(self)
        self.coldButton["text"] = "cold",
        self.coldButton["command"] = self.teaFunctionality.coldPressed
        self.coldButton.pack({"side": "left"})

        #warm button
        self.warmButton = tkinter.Button(self)
        self.warmButton["text"] = "warm",
        self.warmButton["command"] = self.teaFunctionality.warmPressed
        self.warmButton.pack({"side": "left"})

        #should print out the tea from the given entries and buttons
        self.getTeaButton = tkinter.Button(self)
        self.getTeaButton["text"] = "What tea have I made?"
        self.getTeaButton["command"] = self.teaFunctionality.generatePressed
        self.getTeaButton.pack({"side": "left"})

        #text box where the print goes
        self.textBox = Text(self, height = 2, width = 10)
        self.textBox.pack()
'''

