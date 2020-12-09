#################################################
# workspace_mode.py
# this is the mode that runs the entire mindmap with the ability to add tags
# and create new notes
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

import datetime, math

class WorkspaceMode(Mode):

    NOTE_OBJECTS = {Note('Note1', '', [], []), Note('Note2', '', [], []),
                    Note('Note3', '', [], []), Note('Note4', '', [], []), 
                    Note('Note5', '', [], []), Note('Note6', '', [], []),
                    Note('Note7', '', [], []), Note('Note8', '', [], []),
                    Note('Note9', '', [], []), Note('Note10', '', [], [])}
    ACTIVE_NOTE = None

    NOTES = {
                'Note1': ['Note2', 'Note3', 'Note10'], 
                'Note2': ['Note1'], 
                'Note3': ['Note1'],
                'Note4': ['Note5', 'Note6', 'Note7'],
                'Note5': ['Note4'], 
                'Note6': ['Note4'],
                'Note7': ['Note4'],
                'Note8': ['Note9', 'Note10'], 
                'Note9': ['Note8', 'Note10'],
                'Note10': ['Note8', 'Note9', 'Note1']
            }
    WORKSPACE_NAME = 'Name'
    TAGS = {
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
    TAG_COLOR_BANK = ['peachpuff', 'navajo white', 'lemon chiffon', 
                            'DarkSeaGreen1', 'azure', 'alice blue', 
                            'lavender', 'lavender blush', 'misty rose', 
                            'plum1']
    TAG_LOCATIONS = {}
    NOTE_TAGS = { 
                    'Note1': ['biology', 'english'], 
                    'Note2': ['history', 'economics', 
                            'cultural anthropology', 
                            'english', 'physics'], 
                    'Note3': [],
                    'Note4': [],
                    'Note5': ['philosophy', 'physical education', 
                            'chemistry'], 
                    'Note6': ['chemistry'],
                    'Note7': ['artificial intelligence', 'biology'],
                    'Note8': ['physical education'], 
                    'Note9': ['chemistry', 'physics'],
                    'Note10': ['physics']
                }

    NOTE_GROUPS = []
    NOTES_INCLUDED = []
    NOTE_GROUP_LOCATIONS = []
    NOTE_INDIVIDUAL_LOCATIONS = {}

    TAG_PRESSED = {
                        'biology': False, 
                        'physics': False,
                        'chemistry': False, 
                        'english': False, 
                        'artificial intelligence': False,
                        'philosophy': False,
                        'economics': False,
                        'cultural anthropology': False,
                        'history': False,
                        'physical education': False
                    }
    NOTES_HIGHLIGHTED = []

    NOTE_SELECTED = {
                        'Note1': False, 
                        'Note2': False, 
                        'Note3': False,
                        'Note4': False,
                        'Note5': False, 
                        'Note6': False,
                        'Note7': False,
                        'Note8': False, 
                        'Note9': False,
                        'Note10': False
                    }
    ADD_TAG_LOCATIONS = {}

    LOADING_NOTE = False
    WORKSPACE_STARTED = False
    
    def appStarted(mode):
        WorkspaceMode.createNoteGroups()

        mode.createNewNoteButton = Button("Create New Note", (mode.width-190, 
                                    10, mode.width-10, 50))
        mode.instructionsButton = Button("?", (mode.width-240, 10, 
                                    mode.width-200, 50))
        mode.showNoteOptionsBox = False
        mode.noteOptionsBoxLocation = (0,0)
        mode.showAddTagBox = False
        mode.addTagBoxLocation = (0,0)
        mode.openNote = False
        mode.xButton = Button("X", (0,0,0,0))
        mode.makeTagButton = Button("✓", (mode.width-55, mode.height-255, 
                                    mode.width-15, mode.height-225))
        mode.newTagName = Entry('New Tag', (0,0), (mode.width-255, 
                            mode.height-255), 15, 1)
        mode.linkNotes = False
        mode.getMousePressed = False

    @staticmethod
    def createNoteGroups():
        WorkspaceMode.NOTE_GROUPS = []
        WorkspaceMode.NOTES_INCLUDED = []
        WorkspaceMode.NOTE_GROUP_LOCATIONS = []
        for note in WorkspaceMode.NOTES:
            if (note not in WorkspaceMode.NOTES_INCLUDED):
                for group in range(len(WorkspaceMode.NOTE_GROUPS)):
                    for noteLink in WorkspaceMode.NOTES[note]:
                        if (noteLink in WorkspaceMode.NOTE_GROUPS[group]):
                            WorkspaceMode.NOTE_GROUPS[group].append(note)
                            WorkspaceMode.NOTES_INCLUDED.append(note)
                            WorkspaceMode.NOTE_GROUP_LOCATIONS.append([])
                if (note not in WorkspaceMode.NOTES_INCLUDED):    
                    WorkspaceMode.NOTE_GROUPS.append([note])
                    WorkspaceMode.NOTES_INCLUDED.append(note)
                    WorkspaceMode.NOTE_GROUP_LOCATIONS.append([])
            for group in range(len(WorkspaceMode.NOTE_GROUPS)):
                if (note in WorkspaceMode.NOTE_GROUPS[group]):
                    groupNum = group
            for noteLink in WorkspaceMode.NOTES[note]:
                if (noteLink not in WorkspaceMode.NOTES_INCLUDED):
                    WorkspaceMode.NOTE_GROUPS[groupNum].append(noteLink)
                    WorkspaceMode.NOTES_INCLUDED.append(noteLink)
                elif (noteLink not in WorkspaceMode.NOTE_GROUPS[groupNum]):
                    for group in range(len(WorkspaceMode.NOTE_GROUPS)):
                        if (noteLink in WorkspaceMode.NOTE_GROUPS[group]):
                            otherGroupNum = group
                    WorkspaceMode.NOTE_GROUPS[otherGroupNum].extend(WorkspaceMode.NOTE_GROUPS[groupNum])
                    WorkspaceMode.NOTE_GROUPS.pop(groupNum)
                    WorkspaceMode.NOTE_GROUP_LOCATIONS.pop()

    # From: https://www.cs.cmu.edu/~112/notes/quiz7a.html 
    def distance(mode, x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def mousePressed(mode, event):
        if (mode.getMousePressed == True):
            return event.x, event.y

        if (mode.createNewNoteButton.isOnButton(event)):
            mode.showNoteOptionsBox = False
            mode.showAddTagBox = False
            mode.app.setActiveMode(mode.app.runNoteMode)
        elif (mode.instructionsButton.isOnButton(event)):
            mode.showNoteOptionsBox = False
            mode.showAddTagBox = False
            WorkspaceMode.WORKSPACE_STARTED = True
            mode.app.setActiveMode(mode.app.runInstructionsMode)
        elif (mode.makeTagButton.isOnButton(event)):
            WorkspaceMode.TAGS[mode.newTagName.input] = WorkspaceMode.TAG_COLOR_BANK[0]
            WorkspaceMode.TAG_COLOR_BANK.pop(0)
            WorkspaceMode.TAG_PRESSED[mode.newTagName.input] = False
            mode.newTagName.input = ''
            mode.newTagName.isTyping = False
        elif ((mode.width-265 <= event.x <= mode.width-65) 
            and (mode.height-255 <= event.y <= mode.height-225)):
            mode.newTagName.isTyping = True

        for note in WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS:
            if (mode.distance(event.x, event.y, 
                            WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][0],
                            WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][1]) 
                            <= 10):
                if ((WorkspaceMode.NOTE_SELECTED[note] == False) 
                    and (mode.linkNotes == False)):
                    for otherNote in WorkspaceMode.NOTE_SELECTED:
                        WorkspaceMode.NOTE_SELECTED[otherNote] = False
                    mode.showNoteOptionsBox = True
                    if (WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][0]+250 > mode.width):
                        mode.noteOptionsBoxLocation = (WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][0]-250, 
                                                    WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][1])
                    else:
                        mode.noteOptionsBoxLocation = (WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][0]+50, 
                                                    WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][1])
                    WorkspaceMode.NOTE_SELECTED[note] = True

        for note in WorkspaceMode.NOTE_SELECTED:
            if (WorkspaceMode.NOTE_SELECTED[note] == True):
                if (mode.showNoteOptionsBox == True):
                    if ((mode.noteOptionsBoxLocation[0] <= event.x <= mode.noteOptionsBoxLocation[0]+210)
                        and (mode.noteOptionsBoxLocation[1] <= event.y <= mode.noteOptionsBoxLocation[1]+50)):
                        mode.showNoteOptionsBox = False
                        for noteObject in WorkspaceMode.NOTE_OBJECTS:
                            if (note == str(noteObject)):
                                WorkspaceMode.ACTIVE_NOTE = noteObject
                        WorkspaceMode.NOTE_SELECTED[note] = False
                        WorkspaceMode.LOADING_NOTE = True
                        mode.app.setActiveMode(mode.app.runNoteMode)
                    elif ((mode.noteOptionsBoxLocation[0] <= event.x <= mode.noteOptionsBoxLocation[0]+210)
                        and (mode.noteOptionsBoxLocation[1]+50 <= event.y <= mode.noteOptionsBoxLocation[1]+100)):
                        mode.showAddTagBox = True
                        if (WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][0]+250 > mode.width):
                            mode.addTagBoxLocation = (WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][0]-250, 
                                                        WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][1])
                        else:
                            mode.addTagBoxLocation = (WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][0]+50, 
                                                        WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note][1])
                        mode.showNoteOptionsBox = False
                        return # stop clicking blue underneath and add tag box not showing up
                    elif ((mode.noteOptionsBoxLocation[0] <= event.x <= mode.noteOptionsBoxLocation[0]+210)
                        and (mode.noteOptionsBoxLocation[1]+100 <= event.y <= mode.noteOptionsBoxLocation[1]+150)):
                        mode.linkNotes = True
                        mode.showNoteOptionsBox = False
                        return
                    elif ((mode.noteOptionsBoxLocation[0] <= event.x <= mode.noteOptionsBoxLocation[0]+210)
                        and (mode.noteOptionsBoxLocation[1]+150 <= event.y <= mode.noteOptionsBoxLocation[1]+200)):
                        WorkspaceMode.NOTES.pop(note)
                        for noteObject in WorkspaceMode.NOTE_OBJECTS:
                            if (note == str(noteObject)):
                                toRemove = noteObject
                        WorkspaceMode.NOTE_OBJECTS.remove(toRemove)
                        for otherNote in WorkspaceMode.NOTES:
                            if (note in WorkspaceMode.NOTES[otherNote]):
                                WorkspaceMode.NOTES[otherNote].remove(note)
                        WorkspaceMode.NOTE_TAGS.pop(note)
                        WorkspaceMode.NOTE_SELECTED.pop(note)
                        WorkspaceMode.createNoteGroups()
                        WorkspaceMode.NOTE_SELECTED[note] = False
                        mode.showNoteOptionsBox = False
                        return
                    elif (mode.xButton.isOnButton(event)):
                        WorkspaceMode.NOTE_SELECTED[note] = False
                        mode.showNoteOptionsBox = False
                
                if (mode.showAddTagBox == True):
                    for tag in WorkspaceMode.ADD_TAG_LOCATIONS:
                        if ((WorkspaceMode.ADD_TAG_LOCATIONS[tag][0] <= event.x <= WorkspaceMode.ADD_TAG_LOCATIONS[tag][2])
                            and (WorkspaceMode.ADD_TAG_LOCATIONS[tag][1] <= event.y <= WorkspaceMode.ADD_TAG_LOCATIONS[tag][3])):
                            if (tag not in WorkspaceMode.NOTE_TAGS[note]):
                                WorkspaceMode.NOTE_TAGS[note].append(tag)
                                if (WorkspaceMode.TAG_PRESSED[tag] == True):
                                    WorkspaceMode.NOTES_HIGHLIGHTED.append(note)
                            else:
                                WorkspaceMode.NOTE_TAGS[note].remove(tag)
                                if (WorkspaceMode.TAG_PRESSED[tag] == True):
                                    WorkspaceMode.NOTES_HIGHLIGHTED.remove(note)
                            WorkspaceMode.NOTE_SELECTED[note] = False
                            mode.showAddTagBox = False
                            return
                    if (mode.xButton.isOnButton(event)):
                        WorkspaceMode.NOTE_SELECTED[note] = False
                        mode.showAddTagBox = False
                
                if (mode.linkNotes == True):
                    if (mode.xButton.isOnButton(event)):
                        WorkspaceMode.NOTE_SELECTED[note] = False
                        mode.linkNotes = False
                    else:
                        mode.getMousePressed = True
                        noteToLinkX, noteToLinkY = mode.mousePressed(event)
                        mode.getMousePressed = False
                        for noteToLink in WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS:
                            if (mode.distance(noteToLinkX, noteToLinkY, 
                            WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[noteToLink][0],
                            WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[noteToLink][1]) 
                            <= 10):
                                if (noteToLink not in WorkspaceMode.NOTES[note]):
                                    WorkspaceMode.NOTES[noteToLink].append(note)
                                    WorkspaceMode.NOTES[note].append(noteToLink)
                                else:
                                    WorkspaceMode.NOTES[noteToLink].remove(note)
                                    WorkspaceMode.NOTES[note].remove(noteToLink)
                        WorkspaceMode.createNoteGroups()
                        mode.linkNotes = False
                        WorkspaceMode.NOTE_SELECTED[note] = False
                        return

        for tag in WorkspaceMode.TAG_LOCATIONS:
            if ((WorkspaceMode.TAG_LOCATIONS[tag][0] <= event.x <= WorkspaceMode.TAG_LOCATIONS[tag][2])
                and WorkspaceMode.TAG_LOCATIONS[tag][1] <= event.y <= WorkspaceMode.TAG_LOCATIONS[tag][3]):
                if (WorkspaceMode.TAG_PRESSED[tag] == False):
                    WorkspaceMode.NOTES_HIGHLIGHTED = []
                    for note in WorkspaceMode.NOTE_TAGS:
                        if (tag in WorkspaceMode.NOTE_TAGS[note]):
                            WorkspaceMode.NOTES_HIGHLIGHTED.append(note)
                    for otherTag in WorkspaceMode.TAG_PRESSED:
                        WorkspaceMode.TAG_PRESSED[otherTag] = False
                    WorkspaceMode.TAG_PRESSED[tag] = True
                else:
                    WorkspaceMode.TAG_PRESSED[tag] = False
                    WorkspaceMode.NOTES_HIGHLIGHTED = []

    def mouseMoved(mode, event):
        if (mode.createNewNoteButton.isOnButton(event)):
            mode.createNewNoteButton.buttonColor = 'light blue'
        elif (not mode.createNewNoteButton.isOnButton(event)):
            mode.createNewNoteButton.buttonColor = 'white'

        if (mode.instructionsButton.isOnButton(event)):
            mode.instructionsButton.buttonColor = 'light blue'
        elif (not mode.instructionsButton.isOnButton(event)):
            mode.instructionsButton.buttonColor = 'white'

        if (mode.makeTagButton.isOnButton(event)):
            mode.makeTagButton.buttonColor = 'light blue'
        elif (not mode.makeTagButton.isOnButton(event)):
            mode.makeTagButton.buttonColor = 'white'

    def keyPressed(mode, event):
        if (mode.newTagName.isTyping == True):
            mode.newTagName.typing(event)

    # Algorithm for rows and columns layout inspired by:
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    def drawMap(mode, canvas):
        numGroups = len(WorkspaceMode.NOTE_GROUPS)
        numRows = math.floor(math.sqrt(numGroups))
        maxGroupsPerRow = math.ceil(numGroups/numRows)

        rowCount = 0
        groupCountPerRow = 0
        totalGroupCount = 0

        for noteGroup in WorkspaceMode.NOTE_GROUPS:

            dAngle = 2 * math.pi / len(noteGroup)
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

            groupR *= 0.6

            for note in range(len(noteGroup)):
                noteName = noteGroup[note]
                numnotes = len(noteGroup)
                mode.drawDot(canvas, dAngle, groupR, groupCx, groupCy, note, 
                                numnotes, totalGroupCount, noteName)
            if (groupCountPerRow == (maxGroupsPerRow - 1)):
                groupCountPerRow = 0
                rowCount += 1
            else:
                groupCountPerRow += 1

            totalGroupCount += 1

        mode.drawConnections(canvas)
    
    # Algorithm for drawing notes inspired by clock creation inspired by:
    # https://www.cs.cmu.edu/~112/notes/notes-graphics.html#clocksExample
    def drawDot(mode, canvas, dAngle, groupR, groupCx, groupCy, note, numnotes, 
                currentGroup, noteName):
        noteR = 10

        if (numnotes == 1):
            canvas.create_oval(groupCx-noteR, groupCy-noteR, groupCx+noteR, 
                                groupCy+noteR, fill='black')
            WorkspaceMode.NOTE_GROUP_LOCATIONS[currentGroup].append((groupCx, groupCy))
            WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[noteName] = (groupCx, groupCy)
            canvas.create_text(groupCx, groupCy+20, text=noteName,  
                                font='Gilroy 10', fill='gray20')
        else:
            noteAngle = math.pi/2 - dAngle * note
            noteCx = groupCx + groupR * math.cos(noteAngle)
            noteCy = groupCy - groupR * math.sin(noteAngle)
            canvas.create_oval(noteCx-noteR, noteCy-noteR, noteCx+noteR, 
                                noteCy+noteR, fill='black')
            WorkspaceMode.NOTE_GROUP_LOCATIONS[currentGroup].append((noteCx, noteCy))
            WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[noteName] = (noteCx,noteCy)
            canvas.create_text(noteCx, noteCy+20, text=noteName, 
                                font='Gilroy 10', fill='gray20')

    def drawConnections(mode, canvas):
        for note in WorkspaceMode.NOTES:
            for linkedNote in WorkspaceMode.NOTES[note]:
                linkStartX, linkStartY = WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note]
                linkEndX, linkEndY = WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[linkedNote]
                canvas.create_line(linkStartX, linkStartY, linkEndX, linkEndY,
                                    fill='black')

    def drawHighlightedTags(mode, canvas):
        noteR = 10

        for tag in WorkspaceMode.TAG_PRESSED:
            if (WorkspaceMode.TAG_PRESSED[tag] == True):
                color = WorkspaceMode.TAGS[tag]
        for note in WorkspaceMode.NOTES_HIGHLIGHTED:
            noteCx, noteCy = WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note]
            canvas.create_oval(noteCx-noteR, noteCy-noteR, noteCx+noteR, 
                                noteCy+noteR, fill=color)
            canvas.create_text(noteCx, noteCy+20, text=note, 
                                font='Gilroy 10', fill='gray20')
        for note in WorkspaceMode.NOTES:
            if (note not in WorkspaceMode.NOTES_HIGHLIGHTED):
                noteCx, noteCy = WorkspaceMode.NOTE_INDIVIDUAL_LOCATIONS[note]
                canvas.create_oval(noteCx-noteR, noteCy-noteR, noteCx+noteR, 
                                    noteCy+noteR, fill='black')
                canvas.create_text(noteCx, noteCy+20, text=note, 
                                    font='Gilroy 10', fill='gray20')

    def drawTagBox(mode, canvas):
        canvas.create_rectangle(15, mode.height-215, mode.width-15, 
                                    mode.height-15, fill='white smoke')
        dx = dy = 0
        for tag in WorkspaceMode.TAGS:
            tagSize = len(tag) * 12

            if (35 + tagSize + dx > mode.width-35): 
                dy += 45
                dx = 0
            
            if(mode.height - 170 + dy <= mode.height-30):
                canvas.create_rectangle(35+dx, mode.height-200+dy, 
                                        35+tagSize+dx, mode.height-170+dy, 
                                        fill=WorkspaceMode.TAGS[tag], 
                                        outline=WorkspaceMode.TAGS[tag])
                canvas.create_text(35+tagSize/2+dx, mode.height-195+dy, 
                                    text=tag, font='Menlo 15 bold', anchor=N, 
                                    fill='gray20')
                WorkspaceMode.TAG_LOCATIONS[tag] = (25+dx, mode.height-200+dy, 
                                            35+tagSize+dx, mode.height-170+dy)
                dx += tagSize + 20
        
        canvas.create_rectangle(mode.width-265, mode.height-255, mode.width-65, 
                                    mode.height-225, fill='white')
        canvas.create_text(mode.width-275, mode.height-240, 
                            text='Create New Tag:', font='Gilroy 20', 
                            fill='gray20', anchor=E)
    
    def drawNoteOptionsBox(mode, canvas):
        canvas.create_rectangle(mode.noteOptionsBoxLocation[0], 
                                    mode.noteOptionsBoxLocation[1], 
                                    mode.noteOptionsBoxLocation[0]+210, 
                                    mode.noteOptionsBoxLocation[1]+50, 
                                    fill='white')
        canvas.create_text(mode.noteOptionsBoxLocation[0]+105, 
                           mode.noteOptionsBoxLocation[1]+25, 
                           text='Open Note', font='Gilroy 15', fill='gray20')
        canvas.create_rectangle(mode.noteOptionsBoxLocation[0], 
                                    mode.noteOptionsBoxLocation[1]+50, 
                                    mode.noteOptionsBoxLocation[0]+210, 
                                    mode.noteOptionsBoxLocation[1]+100, 
                                    fill='white')
        canvas.create_text(mode.noteOptionsBoxLocation[0]+105, 
                           mode.noteOptionsBoxLocation[1]+75, 
                           text='Tag', font='Gilroy 15', fill='gray20')
        canvas.create_rectangle(mode.noteOptionsBoxLocation[0], 
                                    mode.noteOptionsBoxLocation[1]+100, 
                                    mode.noteOptionsBoxLocation[0]+210, 
                                    mode.noteOptionsBoxLocation[1]+150, 
                                    fill='white')
        canvas.create_text(mode.noteOptionsBoxLocation[0]+105, 
                           mode.noteOptionsBoxLocation[1]+125, 
                           text='Link/Unlink', font='Gilroy 15', fill='gray20')
        canvas.create_rectangle(mode.noteOptionsBoxLocation[0], 
                                    mode.noteOptionsBoxLocation[1]+150, 
                                    mode.noteOptionsBoxLocation[0]+210, 
                                    mode.noteOptionsBoxLocation[1]+200, 
                                    fill='white')
        canvas.create_text(mode.noteOptionsBoxLocation[0]+105, 
                           mode.noteOptionsBoxLocation[1]+175, 
                           text='Delete Note', font='Gilroy 15', fill='gray20')

        mode.xButton.location = mode.noteOptionsBoxLocation[0]-30, \
                                      mode.noteOptionsBoxLocation[1]-30, \
                                      mode.noteOptionsBoxLocation[0], \
                                      mode.noteOptionsBoxLocation[1] 
        mode.xButton.makeButton(canvas)

    def drawAddTagBox(mode, canvas):
        canvas.create_rectangle(mode.addTagBoxLocation[0], 
                                    mode.addTagBoxLocation[1], 
                                    mode.addTagBoxLocation[0]+210, 
                                    mode.addTagBoxLocation[1]+210, 
                                    fill='white')
        canvas.create_text(mode.addTagBoxLocation[0]+105, 
                            mode.addTagBoxLocation[1]+20,
                            text='Add/Remove Tag', font='Gilroy 15')

        dx = dy = 0                   
        for tag in WorkspaceMode.TAGS:
            if (mode.addTagBoxLocation[0] + 40 + dx > mode.addTagBoxLocation[0]+200):
                dy += 40
                dx = 0

            if (mode.addTagBoxLocation[1] + 70 + dy <= mode.addTagBoxLocation[1]+200):
                canvas.create_rectangle(mode.addTagBoxLocation[0]+10+dx, 
                                        mode.addTagBoxLocation[1]+40+dy,
                                        mode.addTagBoxLocation[0]+40+dx, 
                                        mode.addTagBoxLocation[1]+70+dy,
                                        fill=WorkspaceMode.TAGS[tag])
                WorkspaceMode.ADD_TAG_LOCATIONS[tag] = (mode.addTagBoxLocation[0]+10+dx, 
                                                        mode.addTagBoxLocation[1]+40+dy,
                                                        mode.addTagBoxLocation[0]+40+dx, 
                                                        mode.addTagBoxLocation[1]+70+dy)
                dx += 40
        
        mode.xButton.location = mode.addTagBoxLocation[0], \
                                      mode.addTagBoxLocation[1], \
                                      mode.addTagBoxLocation[0] + 30, \
                                      mode.addTagBoxLocation[1] + 30 
        mode.xButton.makeButton(canvas)

    def drawAddLinkBox(mode, canvas):
        canvas.create_rectangle(mode.noteOptionsBoxLocation[0], 
                                    mode.noteOptionsBoxLocation[1], 
                                    mode.noteOptionsBoxLocation[0]+210, 
                                    mode.noteOptionsBoxLocation[1]+50, 
                                    fill='white')
        canvas.create_text(mode.noteOptionsBoxLocation[0]+105, 
                           mode.noteOptionsBoxLocation[1]+25, 
                           text='Click on another note.', font='Gilroy 15', 
                           fill='gray20')
        
        mode.xButton.location = mode.noteOptionsBoxLocation[0]-30, \
                                      mode.noteOptionsBoxLocation[1]-30, \
                                      mode.noteOptionsBoxLocation[0], \
                                      mode.noteOptionsBoxLocation[1] 
        mode.xButton.makeButton(canvas)

    def drawButtons(mode, canvas):
        mode.createNewNoteButton.makeButton(canvas)
        mode.instructionsButton.makeButton(canvas)
        mode.makeTagButton.makeButton(canvas)

    def drawInput(mode, canvas):
        mode.newTagName.showTyping(canvas)

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')
        canvas.create_text(20, 35, text=WorkspaceMode.WORKSPACE_NAME, 
                            font='Gilroy 30 bold', fill='gray20', anchor=W)
        mode.drawMap(canvas)
        mode.drawHighlightedTags(canvas)
        mode.drawTagBox(canvas)
        mode.drawButtons(canvas)
        mode.drawInput(canvas)
    
        if (mode.showNoteOptionsBox == True):
            mode.drawNoteOptionsBox(canvas)
            
        if (mode.showAddTagBox == True):
            mode.drawAddTagBox(canvas)
        
        if (mode.linkNotes == True):
            mode.drawAddLinkBox(canvas)


