#################################################
# workspace_mode.py
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

from cmu_112_graphics import *
from button import Button
from entry import Entry
import datetime

class WorkspaceMode(Mode):

    def appStarted(mode):
        mode.nodeLocations = []
        mode.numNodes = 0

    def mousePressed(mode, event):
        pass

    def keyPressed(mode, event):
        pass

    def drawMap(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')
        for num in range(mode.numNodes):
            
        
    def redrawAll(mode, canvas):
        newNode = str(input())
        if newNode == 'y':
            mode.numNodes += 1
        mode.drawMap(canvas)

#runApp(width=1000, height=700)

