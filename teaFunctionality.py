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
        root = tkinter.Tk()
        self.model = teaClass.Tea()
        self.view = aGUI.aGUI(self)
        self.view.mainloop()
        root.destroy()

    def teaBaseS(self):
        return !(self.view.baseEntry.get() == "")
        
    def milkPressed(self):
        if teaBaseS() == True:
            model.setMilk(True)
            

