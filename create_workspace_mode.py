#################################################
# create_workspace_mode.py
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

from cmu_112_graphics import *
from button import Button
from entry import Entry
import datetime

class CreateWorkspaceMode(Mode):

    def appStarted(mode):
        mode.newWorkspaceName = Entry('New Workspace Name: ', (50,150), (300, 150))
        mode.newWorkspaceDescription = Entry('New Workspace Description: ', 
                                            (50, 200), (350, 200))
        mode.date = datetime.datetime.now()
        mode.dateString = (f'{mode.date.strftime("%A")}, '
                            f'{mode.date.strftime("%B")} ' 
                            f'{mode.date.strftime("%d")}, '
                            f'{mode.date.strftime("%Y")}')

    def mousePressed(mode, event):
        pass

    def keyPressed(mode, event):
        mode.newWorkspaceName.typing(event)

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
        mode.newWorkspaceName.showTyping(canvas)

    def drawInputBoxes(mode, canvas):
        mode.newWorkspaceName.showInputBox(canvas)
        mode.newWorkspaceDescription.showInputBox(canvas)
        
    def redrawAll(mode, canvas):
        mode.drawCreateWorkspaceScreen(canvas)
        mode.drawInputBoxes(canvas)
        mode.drawInput(canvas)

#runApp(width=1000, height=700)

