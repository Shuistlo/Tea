"""
Maybe i'll make a tea class
"""
import tkinter
import aGUI
import teaClass

class teaFunctionanlity:
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
        self.model = teaClass.Tea()
        self.view = aGUI.aGUI(self)
        self.view.mainloop()
        root.destroy()

    def teaBaseS(self):
        '''
        cant make tea unless you have a base
        '''
        return !(self.view.baseEntry.get() == "")
        
    def milkPressed(self):
        if teaBaseS():
            if milkCounter%2 == 1:
                self.model.setMilk(True)
                milkCounter++
            else:
                self.model.setMilk(False)
                milkCounter++

    def hotPressed(self):
        if teaBaseS():
            self.model.setTemp("hot")

    def coldPressed(self):
        if teaBaseS():
            self.model.setTemp("cold")

    def warmPressed(self):
        if teaBaseS():
            self.model.setTemp("warm")

    def getTeaPressed(self):
        self.view.textBox.delete(0, self.lastStringIndex)
        if !teaBaseS():
            self.model.setBase(self.view.baseEntry.get())
            if self.view.sugarEntry.get() != 0:
                self.model.setSugar(self.view.sugarEntry.get())
            if self.view.sizeEntry.get(() != 0:
                self.model.setSize(self.view.sizeEntry.get(())
            self.view.textBox.insert(End, #need a way to put in the string interpretation here
            self.lastStringIndex = #string interpretation's length                        
        else:
            self.view.textBox.insert(END, self.error)
            self.lastStringIndex = len(error)-1

