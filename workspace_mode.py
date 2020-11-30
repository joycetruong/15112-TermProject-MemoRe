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
import datetime, math

class WorkspaceMode(Mode):

    def appStarted(mode):
        mode.nodeGroups = [ [1,2,3,4,5],
                            [1,2,3,4],
                            [1,2,3],
                            [1,2],
                            [1],
                            [1,2,3,4,5],
                            [1,2,3,4],
                            [1,2,3],
                            [1,2],
                            [1]]
        mode.nodeLocations = [[], 
                              [], 
                              [], 
                              [], 
                              [], 
                              [], 
                              [], 
                              [], 
                              [], 
                              []]


    def mousePressed(mode, event):
        pass

    def keyPressed(mode, event):
        pass

    def drawMap(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')

        numGroups = len(mode.nodeGroups)
        numRows = math.floor(math.sqrt(numGroups))
        maxGroupsPerRow = math.ceil(numGroups/numRows)
        rowCount = 0
        groupCountPerRow = 0
        totalGroupCount = 0

        for nodeGroup in mode.nodeGroups:

            dAngle = 2 * math.pi / len(nodeGroup)
            groupR = min((mode.width / maxGroupsPerRow / 2), 
                        (mode.height / numRows / 2))
            margin = max(((mode.height - (groupR * 2 * numRows)) / 2), 
                            ((mode.width - (groupR * 2 * maxGroupsPerRow)) / 2))
            if (margin == ((mode.height - (groupR * 2 * numRows)) / 2)):
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
                mode.drawConnections(canvas)

            if (groupCountPerRow == (maxGroupsPerRow - 1)):
                groupCountPerRow = 0
                rowCount += 1
            else:
                groupCountPerRow += 1

            totalGroupCount += 1
    
    def drawDot(mode, canvas, dAngle, groupR, groupCx, groupCy, node, numNodes, 
                currentGroup):
        nodeR = 5

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

    def drawConnections(mode, canvas):
        for nodeGroup in mode.nodeLocations:
            for nodeX,nodeY in nodeGroup:
                for node in range(len(nodeGroup)):
                    canvas.create_line(nodeX, nodeY, nodeGroup[node][0],
                                        nodeGroup[node][1], fill='black')

    def redrawAll(mode, canvas):
        mode.drawMap(canvas)

#runApp(width=1000, height=700)

