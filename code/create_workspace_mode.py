#################################################
# create_workspace_mode.py
# this is the create workspace screen that will allow us to create a new
# workspace
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
import datetime
from workspace_mode import WorkspaceMode

# Fix button text color once pressed + hover color
class CreateWorkspaceMode(Mode):

    def appStarted(mode):
        mode.newWorkspaceName = Entry('New Workspace Name: ', (50,150), 
                                        (300, 140), 38, 1)
        mode.newWorkspaceDescription = Entry('New Workspace Description: ', 
                                            (50, 225), (350, 215), 38, 6)
        mode.date = datetime.datetime.now()
        mode.dateString = (f'{mode.date.strftime("%A")}, '
                            f'{mode.date.strftime("%B")} ' 
                            f'{mode.date.strftime("%d")}, '
                            f'{mode.date.strftime("%Y")}')
        mode.goHomeButton = Button("Go Home", 
                                (50, mode.height-90, 150, mode.height-50))
        mode.createWorkspaceButton = Button("Create Workspace", 
                                (mode.width-200, mode.height-90, mode.width-50, 
                                    mode.height-50))

    def mouseMoved(mode, event):
        if (mode.goHomeButton.isOnButton(event)):
            mode.goHomeButton.buttonColor = 'light blue'
        elif (not mode.goHomeButton.isOnButton(event)):
            mode.goHomeButton.buttonColor = 'white'
        
        if (mode.createWorkspaceButton.isOnButton(event)):
            mode.createWorkspaceButton.buttonColor = 'light blue'
        elif (not mode.createWorkspaceButton.isOnButton(event)):
            mode.createWorkspaceButton.buttonColor = 'white'

    def mousePressed(mode, event):
        if ((mode.newWorkspaceName.inputLocation[0]-15 <= event.x <= 
            mode.newWorkspaceName.inputLocation[0]+475)
            and (mode.newWorkspaceName.inputLocation[1]-5 <= event.y <= 
            mode.newWorkspaceName.inputLocation[1]+30)):
            mode.newWorkspaceName.isTyping = True
            mode.newWorkspaceDescription.isTyping = False
        elif ((mode.newWorkspaceDescription.inputLocation[0]-15 <= event.x <= 
            mode.newWorkspaceDescription.inputLocation[0]+475)
            and (mode.newWorkspaceDescription.inputLocation[1]-5 <= event.y <= 
            mode.newWorkspaceDescription.inputLocation[1]+150)):
            mode.newWorkspaceDescription.isTyping = True
            mode.newWorkspaceName.isTyping = False
        elif (mode.goHomeButton.isOnButton(event)):
            mode.app.setActiveMode(mode.app.runHomescreenMode)
        elif (mode.createWorkspaceButton.isOnButton(event)):
            WorkspaceMode.WORKSPACE_NAME = mode.newWorkspaceName
            mode.app.setActiveMode(mode.app.runWorkspaceMode)

    def keyPressed(mode, event):
        mode.newWorkspaceName.typing(event)
        mode.newWorkspaceDescription.typing(event)

    def drawCreateWorkspaceScreen(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')
        canvas.create_text(50, 75, text='Create a New Workspace', 
                            font='Gilroy 40', fill='gray20', anchor=W)
        canvas.create_text(50, 450, text='New Workspace Date:  ',
                            font='Gilroy 20 bold', fill='gray20', anchor=W) 
        canvas.create_text(275, 450, text=mode.dateString, 
                            font='Gilroy 20', fill='gray20', anchor=W)
        mode.newWorkspaceName.drawInputPrompt(canvas)
        mode.newWorkspaceDescription.drawInputPrompt(canvas)       

    def drawInput(mode, canvas):
        mode.newWorkspaceName.showPromptAnswerTyping(canvas)
        mode.newWorkspaceDescription.showPromptAnswerTyping(canvas)

    def drawInputBoxes(mode, canvas):
        canvas.create_rectangle(mode.newWorkspaceName.inputLocation[0]-15, 
                                mode.newWorkspaceName.inputLocation[1]-5, 
                                mode.newWorkspaceName.inputLocation[0]+475, 
                                mode.newWorkspaceName.inputLocation[1]+30, 
                                fill='white', outline='black')
        canvas.create_rectangle(mode.newWorkspaceDescription.inputLocation[0]-15, 
                                mode.newWorkspaceDescription.inputLocation[1]-5, 
                                mode.newWorkspaceDescription.inputLocation[0]+475, 
                                mode.newWorkspaceDescription.inputLocation[1]+150, 
                                fill='white', outline='black')
    
    def drawButtons(mode, canvas):
        mode.goHomeButton.makeButton(canvas)
        mode.createWorkspaceButton.makeButton(canvas)

    def redrawAll(mode, canvas):
        mode.drawCreateWorkspaceScreen(canvas)
        mode.drawInputBoxes(canvas)
        mode.drawInput(canvas)
        mode.drawButtons(canvas)