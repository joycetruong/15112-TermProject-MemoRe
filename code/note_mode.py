#################################################
# note_mode.py
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

# From CMU 112 Animation Part 1 Notes: 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

from entry import Entry
from button import Button

class NoteMode(Mode):
    
    def appStarted(mode):
        mode.input = Entry('Note Name', (50, 50), (50, 50), 70)
        mode.saveButton = Button("Save", (mode.width-100, mode.height-90, 
                                    mode.width-50, mode.height-50))

    def mousePressed(mode, event):
        if (0 <= event.x <= mode.width-300):
            mode.input.isTyping = True
        elif (mode.saveButton.isOnButton(event)):
            pass

    def keyPressed(mode, event):
        mode.input.typing(event)

    def drawInput(mode, canvas):
        mode.input.showTyping(canvas)
    
    def drawButton(mode, canvas):
        mode.saveButton.makeButton(canvas)

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')
        canvas.create_rectangle(0, 0, mode.width-300, mode.height, fill='white',
                                outline='black')
        mode.drawInput(canvas)
        mode.drawButton(canvas)