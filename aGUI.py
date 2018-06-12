import tkinter
import teaFunctionality

class aGUI(tkinter.Frame):
    
    def __init__(self): #just the gui for now
        tkinter.Frame.__init__(self)
        self.pack()

        #base entry
        self.baseEntry = tkinter.Entry()
        self.baseEntry.insert("", "enter tea base")
        self.baseEntry.pack({"side": "left"})

        #sugar entry box
        self.sugarEntry = tkinter.Entry()
        self.sugarEntry = tkinter.Entry(0, "enter sugar amount")
        self.sugarEntry.pack({"side": "left"})

        #size entry box
        self.sizeEntry = tkinter.Entry()
        self.sizeEntry = tkinter.Entry(0, "enter size")
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
        self.textBox = Text(root)
        self.textBox.pack()

tkinter._test()
