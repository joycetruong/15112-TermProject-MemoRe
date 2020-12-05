#################################################
# workspace_mode.py
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
from note import Note
from create_workspace_mode import CreateWorkspaceMode

import datetime, math

class WorkspaceMode(Mode):

    NOTES = {
                'Note1': ['Note2', 'Note3'], 
                'Note2': ['Note1'], 
                'Note3': ['Note1']
            }

    def appStarted(mode):
        mode.workspaceName = "Workspace Name"
        mode.tags = {
                        'biology': 'salmon', 
                        'physics': 'pale green',
                        'chemistry': 'light sky blue', 
                        'english': 'khaki1', 
                        'artificial intelligence': 'light pink',
                        'philosophy': 'CadetBlue1',
                        'economics': 'sandy brown',
                        'cultural anthropology': 'PaleVioletRed1',
                        'history': 'aquamarine2',
                        'physical education': 'MediumPurple1'
                    }
        mode.tagColorBank = {'peachpuff', 'navajo white', 'lemon chiffon', 
                                'DarkSeaGreen1', 'azure', 'alice blue', 
                                'lavender', 'lavender blush', 'misty rose', 
                                'plum1'}
        mode.tagLocations = {}
        mode.noteTags = { 
                            'Note1': ['biology', 'english'], 
                            'Note2': [], 
                            'Note3': []
                        }
        mode.nodeGroups = [ [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2] ]
        mode.nodeLocations = [[], []]

    def mousePressed(mode, event):
        # if click on dot, can then tag or link
        pass

    def keyPressed(mode, event):
        pass
    
    # Algorithm for rows and columns layout inspired by:
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    def drawMap(mode, canvas):
        numGroups = len(mode.nodeGroups)
        numRows = math.floor(math.sqrt(numGroups))
        maxGroupsPerRow = math.ceil(numGroups/numRows)

        rowCount = 0
        groupCountPerRow = 0
        totalGroupCount = 0

        for nodeGroup in mode.nodeGroups:

            dAngle = 2 * math.pi / len(nodeGroup)
            groupR = min((mode.width / maxGroupsPerRow / 2), 
                        ((mode.height-215) / numRows / 2))
            margin = max((((mode.height-215) - (groupR * 2 * numRows)) / 2), 
                            ((mode.width - (groupR * 2 * maxGroupsPerRow)) / 2))
            if (margin == (((mode.height-215) - (groupR * 2 * numRows)) / 2)):
                groupCx = groupR + 2 * groupR * (groupCountPerRow)
                groupCy = margin + groupR + 2 * groupR * (rowCount)
            else:
                groupCx = margin + groupR + 2 * groupR * (groupCountPerRow)
                groupCy = groupR + 2 * groupR * (rowCount)

            #canvas.create_oval(groupCx-groupR, groupCy-groupR, groupCx+groupR, groupCy+groupR, fill='red')
            groupR *= 0.6

            for node in range(len(nodeGroup)):
                numNodes = len(nodeGroup)
                mode.drawDot(canvas, dAngle, groupR, groupCx, groupCy, node, 
                                numNodes, totalGroupCount)
                #mode.drawConnections(canvas)

            if (groupCountPerRow == (maxGroupsPerRow - 1)):
                groupCountPerRow = 0
                rowCount += 1
            else:
                groupCountPerRow += 1

            totalGroupCount += 1
    
    # Algorithm for drawing nodes inspired by clock creation inspired by:
    # https://www.cs.cmu.edu/~112/notes/notes-graphics.html#clocksExample
    def drawDot(mode, canvas, dAngle, groupR, groupCx, groupCy, node, numNodes, 
                currentGroup):
        nodeR = 10

        if (numNodes == 1):
            canvas.create_oval(groupCx-nodeR, groupCy-nodeR, groupCx+nodeR, 
                                groupCy+nodeR, fill='black')
            mode.nodeLocations[currentGroup].append((groupCx, groupCy))
        else:
            nodeAngle = math.pi/2 - dAngle * node
            nodeX = groupCx + groupR * math.cos(nodeAngle)
            nodeY = groupCy - groupR * math.sin(nodeAngle)
            mode.nodeLocations[currentGroup].append((nodeX, nodeY))
            canvas.create_oval(nodeX-nodeR, nodeY-nodeR, nodeX+nodeR, 
                                nodeY+nodeR, fill='black')

    """ 
    def drawConnections(mode, canvas):
        for nodeGroup in mode.nodeLocations:
            for nodeX,nodeY in nodeGroup:
                for node in range(len(nodeGroup)):
                    canvas.create_line(nodeX, nodeY, nodeGroup[node][0],
                                        nodeGroup[node][1], fill='black')
    """

    def drawTagBox(mode, canvas):
        canvas.create_rectangle(15, mode.height-215, mode.width-15, 
                                    mode.height-15, fill='white smoke')
        dx = dy = 0
        for tag in mode.tags:
            tagSize = len(tag) * 12

            if (35 + tagSize + dx > mode.width-35): 
                dy += 45
                dx = 0
            
            if(mode.height-170+dy <= mode.height-30):
                canvas.create_rectangle(35+dx, mode.height-200+dy, 
                                        35+tagSize+dx, mode.height-170+dy, 
                                        fill=mode.tags[tag], 
                                        outline=mode.tags[tag])
                canvas.create_text(35+tagSize/2+dx, mode.height-195+dy, 
                                    text=tag, font='Menlo 15 bold', anchor=N)
                mode.tagLocations[tag] = (25+dx, mode.height-200+dy, 
                                            35+tagSize+dx, mode.height-170+dy)
                dx += tagSize + 20
        
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')
        canvas.create_text(mode.width/2, 30, text=mode.workspaceName, 
                            font='Gilroy 30 bold')
        mode.drawMap(canvas)
        mode.drawTagBox(canvas)

