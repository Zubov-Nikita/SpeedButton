
from Tkinter import *

class SpeedButton(Button):
    isPressed=False
    pressedColor="red"
    notPressedColor="green"
    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, 'button', cnf, kw)
        self.bind("<Button-1>", self.press)

    def setPressedColor(self,color):
        self.pressedColor=color
        return self

    def setNotPressedColor(self,color):
        self.notPressedColor=color
        return self

    def setColors(self,pressedColor,notPressedColor):
        self.pressedColor=pressedColor
        self.notPressedColor=notPressedColor

    def press(self,event):
        self.isPressed=not self.isPressed 

        if self.isPressed==True:
            self['background']=self.pressedColor           
        else:
            self['background']=self.notPressedColor               

root = Tk()
root.title("Speedbutton")

button=SpeedButton(root,text="test")
button.setPressedColor("gray").setNotPressedColor("orange")
button.pack()

button2=SpeedButton(root,text="test2")
button2.setColors("blue","yellow")
button2.pack()

root.mainloop()

