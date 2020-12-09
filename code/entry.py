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
        self.isHeading = False
        self.lastLineLength = 0
    
    def __repr__(self):
        return self.input

    def typing(self, event):
        bannedKeys = {'Up', 'Down', 'Left', 'Right'}
        if (self.isTyping == True):
            if (event.key == 'Space'):
                self.input += ' '
                self.currentLineLength += 1 
            elif (event.key == 'Delete'):
                if (self.input == ''):
                    pass
                elif ((len(self.input) >= 2) and (self.input[-2] == '`')):
                    self.input = self.input[:-2]
                    self.currentLineLength -= 2
                    if (self.currentLineLength == 0):
                        self.isHeading = False
                elif ((len(self.input) >= 6) 
                    and ((self.input[-6:-1] == '~BLD~') 
                    or (self.input[-6:-1] == '~ITL~'))):
                    self.input = self.input[:-6]
                elif ((len(self.input) >= 6) and (self.input[-6:] == 'DOUB\n\n')):
                    if (self.lastLineLength == 0):
                        self.currentLineLength = 0
                        self.input = self.input[:-6]
                    elif (self.lastLineLength < self.lineLength):
                        self.currentLineLength = self.lastLineLength - 1
                        self.input = self.input[:-8]
                    else:
                        self.currentLineLength = self.lineLength - 1
                        self.input = self.input[:-8]
                    self.isHeading = True
                elif (self.input[-1] == '\n'):
                    if (self.lastLineLength == 0):
                        self.currentLineLength  = 0
                        self.input = self.input[:-1]
                    elif (self.lastLineLength < self.lineLength):
                        self.currentLineLength = self.lastLineLength - 1
                        self.input = self.input[:-2]
                    else:
                        self.currentLineLength = self.lineLength - 1
                        self.input = self.input[:-2]
                    self.isHeading = False
                else:
                    self.input = self.input[:-1]
                    self.currentLineLength -= 1

            elif (event.key == 'Enter'):
                if (self.isHeading == True):
                    self.input += 'DOUB\n\n'
                    self.isHeading = False
                    self.lastLineLength = self.currentLineLength
                    self.currentLineLength = 0
                else:
                    self.input += '\n'
                    self.lastLineLength = self.currentLineLength
                    self.currentLineLength = 0

            elif (event.key in bannedKeys):
                pass
            else:
                if (self.input.count('\n') < self.maxLines):
                    style = self.getStyle()
                    if (style == 'normal'):
                        if (event.key == '??'):
                            pass
                        else:
                            if ((event.key == '#')
                                and (self.currentLineLength == 0)):
                                self.isHeading = True
                            elif (self.isHeading == True):
                                self.input += '`' + event.key
                                self.currentLineLength += 2
                            else:
                                self.input += event.key
                                self.currentLineLength += 1  
                    elif (style == 'bolded'):
                        self.input += '~BLD~' + event.key
                        self.currentLineLength += 1 
                    elif (style == 'italicized'):
                        self.input += '~ITL~' + event.key
                        self.currentLineLength += 1 
                    if (self.currentLineLength >= self.lineLength): 
                        if (self.isHeading == True):
                            self.input += '\n\n'
                            self.lastLineLength = self.lineLength
                            self.currentLineLength = 0
                            self.isHeading = False
                        else:
                            self.input += '\n' 
                            self.lastLineLength = self.lineLength
                            self.currentLineLength = 0 

    def drawInputPrompt(self, canvas):
        canvas.create_text(self.promptLocation[0], self.promptLocation[1], 
                            text=self.label, font='Gilroy 20 bold', 
                            fill='gray20', anchor=W)

    def showTyping(self, canvas):
        writing = []
        index = 0
        while (len(self.input) != index):
            if ((len(self.input) >= 6)
                and ((self.input[index:index+5] == '~BLD~') 
                or (self.input[index:index+5] == '~ITL~'))):
                writing += [self.input[index:index+6]]
                index += 6
            elif ((len(self.input) >= 4) and self.input[index:index+4] == 'DOUB'):
                index += 4
                pass
            elif ((len(self.input) >= 2) and (self.input[index] == '`')):
                writing += [self.input[index:index+2]]
                index += 2
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
                    dx += 12
                elif (char.startswith('~ITL~')):
                    canvas.create_text(xStart+dx, yStart+dy, text=char[-1], 
                                    font='Menlo 20 italic', anchor=NW)
                    dx += 12
                elif (char.startswith('`')):
                    canvas.create_text(xStart+dx, yStart+dy, text=char[-1], 
                                    font='Menlo 40 bold', anchor=NW)
                    dx += 22
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
