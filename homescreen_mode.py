#################################################
# homescreen_mode.py
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

from cmu_112_graphics import *
from button import Button
from entry import Entry
from create_workspace_mode import CreateWorkspaceMode

class HomescreenMode(Mode):

    def appStarted(mode):
        mode.newWorkspaceButton = Button("Create New Workspace", 
                                (mode.width/2-100, 350, mode.width/2+100,400))
        mode.oldWorkspaceButton = Button("Open Exisiting Workspace", 
                                (mode.width/2-100, 425, mode.width/2+100, 475))
        mode.newWorkspaceName = Entry("New Workspace Name", (0,0))
        mode.runCreateWorkspaceMode = CreateWorkspaceMode()

    def mouseMoved(mode, event):
        if (mode.newWorkspaceButton.isOnButton(event)):
            mode.newWorkspaceButton.buttonColor = 'light blue'
        elif (not mode.newWorkspaceButton.isOnButton(event)):
            mode.newWorkspaceButton.buttonColor = 'white'
        
        if (mode.oldWorkspaceButton.isOnButton(event)):
            mode.oldWorkspaceButton.buttonColor = 'light blue'
        elif (not mode.oldWorkspaceButton.isOnButton(event)):
            mode.oldWorkspaceButton.buttonColor = 'white'

    def mousePressed(mode, event):
        if (mode.newWorkspaceButton.isOnButton(event)):
            mode.newWorkspaceButton.buttonColor = 'white'
            mode.newWorkspaceButton.textColor = 'light blue'
            mode.app.setActiveMode(mode.app.runCreateWorkspaceMode)
        elif (mode.oldWorkspaceButton.isOnButton(event)):
            mode.oldWorkspaceButton.buttonColor = 'white'
            mode.oldWorkspaceButton.textColor = 'light blue'

    def keyPressed(mode, event):
        mode.newWorkspaceName.typing(event)

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
        mode.oldWorkspaceButton.makeButton(canvas)

    def redrawAll(mode, canvas):
        mode.drawHomescreen(canvas)
        mode.drawButton(canvas)

    #runmode(width=1000, height=700)