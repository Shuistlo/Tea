import tkinter
import teaFunctionality

class aGUI(tkinter.Frame):
    
    def __init__(self): #just the gui for now
        tkinter.Frame.__init__(self)
        self.pack()

        self.baseEntry = tkinter.Entry()
        self.baseEntry.insert("", "enter tea base")
        self.baseEntry.pack({"side": "left"})

        self.sugarEntry = tkinter.Entry()
        self.sugarEntry = tkinter.Entry(0, "enter sugar amount")
        self.sugarEntry.pack({"side": "left"})

        self.sizeEntry = tkinter.Entry()
        self.sizeEntry = tkinter.Entry(0, "enter size")
        self.sizeEntry.pack({"side": "left"})

        #not sure how to handle toppings

        self.milkButton = tkinter.Button(self)
        self.milkButton["text"] = "got milk",
        self.milkButton["command"] = self.teaFunctionality.milkPressed
        self.milkButton.pack({"side": "left"})

        self.hotButton = tkinter.Button(self)
        self.hotButton["text"] = "hot",
        self.hotButton["command"] = self.teaFunctionality.hotPressed
        self.hotButton.pack({"side": "left"})

        self.coldButton = tkinter.Button(self)
        self.coldButton["text"] = "cold",
        self.coldButton["command"] = self.teaFunctionality.coldPressed
        self.coldButton.pack({"side": "left"})

        self.warmButton = tkinter.Button(self)
        self.warmButton["text"] = "warm",
        self.warmButton["command"] = self.teaFunctionality.warmPressed
        self.warmButton.pack({"side": "left"})

        #need a reset button
        #need a text box

        #what did i make

tkinter._test()
