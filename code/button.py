#################################################
# button.py
# this is the button object that will let me create clickable buttons in my app
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

# From CMU 112 Animation Part 1 Notes: 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

class Button(object):

    def __init__(self, label, location):
        self.label = label
        self.location = location
        self.buttonColor = 'white'
        self.textColor = 'gray20'
    
    def isOnButton(self, event):
        return ((self.location[0] <= event.x <= self.location[2])
                and (self.location[1] <= event.y <= self.location[3]))
    
    def makeButton(self, canvas):
        canvas.create_rectangle(self.location[0], self.location[1],
                                self.location[2], self.location[3], 
                                fill=self.buttonColor, outline='gray20')
        canvas.create_text(self.location[0]+ 
                            (self.location[2]-self.location[0])/2, 
                            self.location[1]+ 
                            (self.location[3]-self.location[1])/2, 
                            text=self.label, font='Gilroy 14', 
                            fill=self.textColor)