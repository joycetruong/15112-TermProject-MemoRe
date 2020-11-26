# entry.py

from cmu_112_graphics import *

class Entry(object):

    def __init__(self, label, promptLocation, inputLocation):
        self.input = ''
        self.label = label
        self.promptLocation = promptLocation
        self.inputLocation = inputLocation
    
    def typing(self, event):
        if (event.key == 'Space'):
            self.input += ' '
        elif (event.key == 'Delete'):
            self.input = self.input[:-1]
        else:
            self.input += event.key
    
    def drawInputPrompt(self, canvas):
        canvas.create_text(self.promptLocation[0], self.promptLocation[1], 
                            text=self.label, font='Gilroy 20 bold', 
                            fill='gray20', anchor=W)

    def showTyping(self, canvas):
        canvas.create_text(self.inputLocation[0], self.inputLocation[1],
                            text=self.input, font='Gilroy 20', anchor=W)

    def showInputBox(self, canvas):
        canvas.create_rectangle(self.inputLocation[0]-15, 
                                self.inputLocation[1]-15, 
                                self.inputLocation[0]+475, 
                                self.inputLocation[1]+15, 
                                fill='white', outline='black')
