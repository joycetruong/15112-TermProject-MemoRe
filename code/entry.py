#################################################
# entry.py
# this is the entry object that will allow me to get user input in the GUI
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

# From CMU 112 Animation Part 1 Notes: 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

class Entry(object):

    def __init__(self, label, promptLocation, inputLocation, lineLength, 
                    maxLines):
        self.input = ''
        self.label = label
        self.promptLocation = promptLocation
        self.inputLocation = inputLocation
        self.lineLength = lineLength
        self.maxLines = maxLines

        self.currentLineLength = 0
        self.isTyping = False
        self.styles = {'normal': True, 
                       'bolded': False, 
                       'italicized': False}
    
    def __repr__(self):
        return self.input

    def typing(self, event):
        bannedKeys = {'Up', 'Down', 'Left', 'Right'}
        if (self.isTyping == True):
            if (event.key == 'Space'):
                self.input += ' '
                self.currentLineLength += 1 
            elif (event.key == 'Delete'):
                if (self.input[-1] == '\n'):
                    self.input = self.input[:-2]
                    self.currentLineLength += self.lineLength - 1
                else:
                    self.input = self.input[:-1]
                    self.currentLineLength -= 1
            elif (event.key == 'Enter'):
                self.input += '\n'
                self.currentLineLength = 0
            elif (event.key in bannedKeys):
                pass
            else:
                if (self.input.count('\n') < self.maxLines):
                    style = self.getStyle()
                    if (style == 'normal'):
                        self.input += event.key
                        self.currentLineLength += 1  
                    elif (style == 'bolded'):
                        self.input += '~BLD~' + event.key
                        self.currentLineLength += 1 
                    elif (style == 'italicized'):
                        self.input += '~ITL~' + event.key
                        self.currentLineLength += 1 
                    if (self.currentLineLength == self.lineLength): 
                        self.input += '\n' 
                        self.currentLineLength = 0 
    
    def drawInputPrompt(self, canvas):
        canvas.create_text(self.promptLocation[0], self.promptLocation[1], 
                            text=self.label, font='Gilroy 20 bold', 
                            fill='gray20', anchor=W)

    def showTyping(self, canvas):
        writing = []
        index = 0
        while (len(self.input) != index):
            if (self.input[index] == '~'):
                writing += [self.input[index:index+6]]
                index += 6
            else:
                 writing += [self.input[index]]
                 index += 1

        xStart,yStart = self.inputLocation
        dx = dy = 0

        for char in writing:
            if (char == '\n'):
                dx = 0
                dy += 25
            else:
                if (char.startswith('~BLD~')):
                    canvas.create_text(xStart+dx, yStart+dy, text=char[-1], 
                                    font='Menlo 20 bold', anchor=NW)
                elif (char.startswith('~ITL~')):
                    canvas.create_text(xStart+dx, yStart+dy, text=char[-1], 
                                    font='Menlo 20 italic', anchor=NW)
                else:
                    canvas.create_text(xStart+dx, yStart+dy, text=char, 
                                    font='Menlo 20', anchor=NW)
                dx += 12

    def showPromptAnswerTyping(self, canvas):
        canvas.create_text(self.inputLocation[0], self.inputLocation[1],
                            text=self.input, font='Menlo 20', anchor=NW)

    def getStyle(self):
        for style in self.styles:
            if (self.styles[style] == True):
                return style
                
    def setStyle(self, newStyle):
        self.styles[self.getStyle()] = False
        self.styles[newStyle] = True
