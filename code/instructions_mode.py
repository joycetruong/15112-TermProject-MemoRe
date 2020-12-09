#################################################
# instructions_mode.py
# this is the mode that gives the user specific instructions to follow
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
from workspace_mode import WorkspaceMode

class InstructionsMode(Mode):

    def appStarted(mode):
        mode.goHomeButton = Button("Go Home", 
                                (50, mode.height-90, 150, mode.height-50))
        mode.backToWorkspaceButton = Button("Back to Workspace", 
                                (mode.width-250, mode.height-90, 
                                mode.width-50, mode.height-50))
    
    def mouseMoved(mode, event):
        if (mode.goHomeButton.isOnButton(event)):
            mode.goHomeButton.buttonColor = 'light blue'
        elif (not mode.goHomeButton.isOnButton(event)):
            mode.goHomeButton.buttonColor = 'white'
        
        if (mode.backToWorkspaceButton.isOnButton(event)):
            mode.backToWorkspaceButton.buttonColor = 'light blue'
        elif (not mode.backToWorkspaceButton.isOnButton(event)):
            mode.backToWorkspaceButton.buttonColor = 'white'

    def mousePressed(mode, event):
        if (mode.goHomeButton.isOnButton(event)):
            mode.app.setActiveMode(mode.app.runHomescreenMode)
        elif ((mode.backToWorkspaceButton.isOnButton(event)) 
            and (WorkspaceMode.WORKSPACE_STARTED == True)):
            mode.app.setActiveMode(mode.app.runWorkspaceMode)
    
    def drawButtons(mode, canvas):
        mode.goHomeButton.makeButton(canvas)
        if (WorkspaceMode.WORKSPACE_STARTED == True):
            mode.backToWorkspaceButton.makeButton(canvas)
    
    def drawInstructions(mode, canvas):
        canvas.create_text(50, 50, text='Instuctions', fill='gray20', 
                            font='Gilroy 30 bold', anchor=W)

        canvas.create_text(50, 100, text='Note the following restrictions: ', 
                            fill='gray20', font='Gilroy 15 bold', anchor=W)
        canvas.create_text(50, 130, text='   -   There is a maximum of 20 tags allowed', 
                            fill='gray20', font='Gilroy 15', anchor=W)
        canvas.create_text(50, 155, text='   -   Please do not type \'~\' or \'`\' in any input box/the text editor', 
                            fill='gray20', font='Gilroy 15', anchor=W)
        canvas.create_text(50, 180, text='   -   Notes are not allowed to have spaces in their names, spaces will be replaced with \'-\'', 
                            fill='gray20', font='Gilroy 15', anchor=W)
        canvas.create_text(50, 205, text='   -   There is no maximum number of notes per group or number of note groups in the mindmap, but too many groups will', 
                            fill='gray20', font='Gilroy 15', anchor=W)
        canvas.create_text(50, 225, text='        mean that the program will not run properly due to overlap.', 
                            fill='gray20', font='Gilroy 15', anchor=W)

        canvas.create_text(50, 275, text='Other things to consider: ', 
                            fill='gray20', font='Gilroy 15 bold', anchor=W)
        canvas.create_text(50, 305, text='   -   If you want to save changes to a note that already exists, when saving, the note\'s name will come up.', 
                            fill='gray20', font='Gilroy 15', anchor=W)
        canvas.create_text(50, 325, text='        Make sure that you do not change the name that pops up and just click save so that it saves as the same note.', 
                            fill='gray20', font='Gilroy 15', anchor=W)
        canvas.create_text(50, 345, text='        Otherwise, saving it by a different name will create a new note.', 
                            fill='gray20', font='Gilroy 15', anchor=W)
        canvas.create_text(50, 370, text='   -   Typing \'#\' on a new line makes that line a header.', 
                            fill='gray20', font='Gilroy 15', anchor=W)

    def redrawAll(mode, canvas):
        mode.drawButtons(canvas)
        mode.drawInstructions(canvas)