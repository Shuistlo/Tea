"""
Maybe i'll make a tea class
"""
from tkinter import *
from teaClass import Tea

class teaFunctionality:
    def __init__(self):
        '''
        starts TK framework
        instantiates model (converter)
        instantiates view (MyFrame)
        starts event loop
        '''
        self.milkCounter = 0;
        self.lastStringIndex = 0;
        self.error = "Tea base not specified!"
        
        root = tkinter.Tk()
        self.model = teaClass.Tea() #want this to make a standard tea object
        self.view = aGUI.aGUI(self)
        self.view.mainloop()
        root.destroy()

    def teaBaseS(self):
        '''
        cant make tea unless you have a base
        '''
        return not (self.view.baseEntry.get() == "")
        
    #has some kind of button counter:
    #odd number of clicks: milk = true
    #maybe should change the button if odd number of clicks like label "milk" becomes "MILK"
    def milkPressed(self):
        if self.teaBaseS():
            if self.milkCounter%2 == 1:
                self.model.setMilk(True)
                self.milkCounter += 1
            else:
                self.model.setMilk(False)
                self.milkCounter += 1

    def hotPressed(self):
        if self.teaBaseS():
            self.model.setTemp("hot")

    def coldPressed(self):
        if self.teaBaseS():
            self.model.setTemp("cold")

    def warmPressed(self):
        if self.teaBaseS():
            self.model.setTemp("warm")

    #creates/updates the tea object and prints it in the textbox. not functioning.
    def getTeaPressed(self):
        self.view.textBox.delete(0, self.lastStringIndex)
        if self.teaBaseS():
            self.model.setBase(self.view.baseEntry.get())
            if self.view.sugarEntry.get() != 0:
                self.model.setSugar(self.view.sugarEntry.get())
            if self.view.sizeEntry.get() != 0:
                self.model.setSize(self.view.sizeEntry.get(()))
            self.view.textBox.insert(END, "test")
            self.lastStringIndex = 0#string interpretation's length
        else:
            self.view.textBox.insert(END, self.error)
            self.lastStringIndex = len(self.error)-1

