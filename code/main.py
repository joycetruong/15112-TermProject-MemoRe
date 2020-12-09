#################################################
# main.py
# this is the main program for my app to be ran and allows for each screen
# mode to be called when necessary --> default is homescreen mode
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
from homescreen_mode import HomescreenMode
from create_workspace_mode import CreateWorkspaceMode
from workspace_mode import WorkspaceMode
from note_mode import NoteMode
from instructions_mode import InstructionsMode

# ModalApp framework inspired by:
# https://github.com/spartace98/15-112-Term-Project/
class Main(ModalApp):
    def appStarted(app):           
        app.runHomescreenMode = HomescreenMode()
        app.runCreateWorkspaceMode = CreateWorkspaceMode()
        app.runInstructionsMode = InstructionsMode()
        app.runWorkspaceMode = WorkspaceMode()
        app.runNoteMode = NoteMode()
        app.setActiveMode(app.runHomescreenMode) # run different modes here

Main(width=1000, height=700)
