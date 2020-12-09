#################################################
# homescreen_mode.py
# this is the starting screen for my app
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

# From CMU 112 Animation Part 1 Notes: 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

# Created by me:
from button import Button
from entry import Entry
from create_workspace_mode import CreateWorkspaceMode

# Fix button text color once pressed + hover color
class HomescreenMode(Mode):

    def appStarted(mode):
        mode.newWorkspaceButton = Button("Create New Workspace", 
                                (mode.width/2-100, 350, mode.width/2+100,400))
        mode.instructionsButton = Button("Instructions", 
                                (mode.width/2-100, 425, mode.width/2+100, 475))
        mode.newWorkspaceButton.textColor = 'gray20'
        mode.newWorkspaceButton.textColor = 'gray20'

    def mouseMoved(mode, event):
        if (mode.newWorkspaceButton.isOnButton(event)):
            mode.newWorkspaceButton.buttonColor = 'light blue'
        elif (not mode.newWorkspaceButton.isOnButton(event)):
            mode.newWorkspaceButton.buttonColor = 'white'
        
        if (mode.instructionsButton.isOnButton(event)):
            mode.instructionsButton.buttonColor = 'light blue'
        elif (not mode.instructionsButton.isOnButton(event)):
            mode.instructionsButton.buttonColor = 'white'

    def mousePressed(mode, event):
        if (mode.newWorkspaceButton.isOnButton(event)):
            mode.app.setActiveMode(mode.app.runCreateWorkspaceMode)
        elif (mode.instructionsButton.isOnButton(event)):
            mode.app.setActiveMode(mode.app.runInstructionsMode)

    def drawHomescreen(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')
        canvas.create_text(mode.width/2, mode.height/2-100, text='MemoRe:', 
                            font='Gilroy 100', fill='gray20')
        canvas.create_line(mode.width/2, 0, mode.width/2, 150, fill='gray20')
        canvas.create_line(mode.width/2, mode.height, mode.width/2, 
                            mode.height-150, fill='gray20')

    def drawButton(mode, canvas):
        mode.newWorkspaceButton.makeButton(canvas)
        mode.instructionsButton.makeButton(canvas)

    def redrawAll(mode, canvas):
        mode.drawHomescreen(canvas)
        mode.drawButton(canvas)
