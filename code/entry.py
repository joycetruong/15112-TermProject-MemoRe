# entry.py

from cmu_112_graphics import *

class Entry(object):

    def __init__(self, label, promptLocation, inputLocation, lineLength):
        self.input = ''
        self.label = label
        self.promptLocation = promptLocation
        self.inputLocation = inputLocation
        self.lineLength = lineLength
        self.isTyping = False
    
    def typing(self, event):
        if (self.isTyping == True):
            if (event.key == 'Space'):
                self.input += ' '
            elif (event.key == 'Delete'):
                self.input = self.input[:-1]
            else:
                if (len(self.input) % self.lineLength == 0):
                    self.input += '\n'
                self.input += event.key
    
    def drawInputPrompt(self, canvas):
        canvas.create_text(self.promptLocation[0], self.promptLocation[1], 
                            text=self.label, font='Gilroy 20 bold', 
                            fill='gray20', anchor=W)

    def showTyping(self, canvas):
        canvas.create_text(self.inputLocation[0], self.inputLocation[1],
                            text=self.input, font='Gilroy 20', anchor=NW)
    
