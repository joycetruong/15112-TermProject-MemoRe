#################################################
# main.py
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

# From CMU 112 website 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

# Created by me
from button import Button
from entry import Entry
from homescreen_mode import HomescreenMode
from create_workspace_mode import CreateWorkspaceMode
from workspace_mode import WorkspaceMode

# trying to make everything into a mode --> does not currently work 
# refer to homescreen mode
class Main(ModalApp):
    def appStarted(app):           
        app.runHomescreenMode = HomescreenMode()
        app.runCreateWorkspaceMode = CreateWorkspaceMode()
        app.runWorkspaceMode = WorkspaceMode()
        app.setActiveMode(app.runWorkspaceMode)

Main(width=1000, height=700)
