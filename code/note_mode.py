#################################################
# note_mode.py
# this is the mode that allows users to create notes in a text editor
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

# From CMU 112 Animation Part 1 Notes: 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

# Created by me:
from entry import Entry
from button import Button
from note import Note
from workspace_mode import WorkspaceMode

class NoteMode(Mode):

    def appStarted(mode):

        mode.name = Entry('Enter Note Name:', (mode.width/2-80, 
                            mode.height/2-30), (mode.width/2-140, 
                            mode.height/2+10), 10, 1)
        mode.input = Entry('Note Input', (50, 50), (50, 50), 49, 24)
        mode.input.isTyping = True
        mode.connections = []
        mode.loadedNote = WorkspaceMode.ACTIVE_NOTE

        mode.saveButton = Button("Save", (mode.width-100, mode.height-80, 
                                    mode.width-40, mode.height-40))
        mode.backButton = Button("Back", (mode.width-260, mode.height-80, 
                                    mode.width-200, mode.height-40))
        mode.boldButton = Button("Bold", (mode.width-260, 40, 
                                    mode.width-40, 80))
        mode.italicizeButton = Button("Italicize", (mode.width-260, 100, 
                                    mode.width-40, 140))
        mode.highlightButton = Button("Highlight", (mode.width-260, 160, 
                                    mode.width-40, 200))
        mode.underlineButton = Button("Underline", (mode.width-260, 220, 
                                    mode.width-40, 260))

        mode.tools = {'highlight': False, 
                      'underline': False}
        
        mode.highlightCoords = []
        mode.underlineCoords = []
        mode.currentCoords = [0, 0, 0, 0]
        mode.askName = False
        mode.enterNameButton = Button("Enter", (mode.width/2+ 60, mode.height/2,
                                mode.width/2+150, mode.height/2+40))

    def loadNote(mode):
        if (mode.loadedNote != None):
            mode.name.input = WorkspaceMode.ACTIVE_NOTE.name
            mode.input.input = WorkspaceMode.ACTIVE_NOTE.input
            mode.highlightCoords = WorkspaceMode.ACTIVE_NOTE.highlights
            mode.underlineCoords = WorkspaceMode.ACTIVE_NOTE.underlines

    def findConnections(mode):
        writing = mode.input.input.split()
        notes = []
        notesUpper = []
        for note in WorkspaceMode.NOTES:
            notes.append(note)
            notesUpper.append(note.upper())

        for word in writing:
            if (word.upper() in notesUpper):
                index = notesUpper.index(word.upper())
                mode.connections.append(notes[index])

    def mousePressed(mode, event):
        if (mode.saveButton.isOnButton(event)):
            mode.askName = True
        elif (mode.enterNameButton.isOnButton(event)):
            mode.findConnections()
            WorkspaceMode.NOTES[str(Note(mode.name.input, mode.input.input,
                                    mode.highlightCoords, 
                                    mode.underlineCoords))] = mode.connections
            WorkspaceMode.NOTE_OBJECTS.add(Note(mode.name.input, 
                                    mode.input.input,
                                    mode.highlightCoords, 
                                    mode.underlineCoords))
            for note in WorkspaceMode.NOTES[str(Note(mode.name.input, 
                                        mode.input.input, mode.highlightCoords, 
                                        mode.underlineCoords))]:
                WorkspaceMode.NOTES[note].append(str(Note(mode.name.input, 
                                        mode.input.input, mode.highlightCoords, 
                                        mode.underlineCoords)))
            WorkspaceMode.NOTE_TAGS[str(Note(mode.name.input, mode.input.input,
                                    mode.highlightCoords, 
                                    mode.underlineCoords))] = []
            WorkspaceMode.NOTE_SELECTED[str(Note(mode.name.input, 
                                        mode.input.input,
                                        mode.highlightCoords, 
                                        mode.underlineCoords))] = False
            WorkspaceMode.createNoteGroups()
            mode.appStarted()
            mode.app.setActiveMode(mode.app.runWorkspaceMode)
        elif (mode.backButton.isOnButton(event)):
            mode.appStarted()
            mode.app.setActiveMode(mode.app.runWorkspaceMode)
        elif (mode.boldButton.isOnButton(event)):
            mode.styleChange(event, mode.boldButton, 'bolded')
        elif (mode.italicizeButton.isOnButton(event)):
            mode.styleChange(event, mode.italicizeButton, 'italicized')
        elif (mode.highlightButton.isOnButton(event)):
            mode.toolChange(event, mode.highlightButton, 'highlight')
        elif (mode.underlineButton.isOnButton(event)):
            mode.toolChange(event, mode.underlineButton, 'underline')
        else:
            if (event.x >= mode.width - 300):
                pass
            else:
                mode.currentCoords[0], mode.currentCoords[1] = event.x, event.y

    def mouseDragged(mode, event):
        if (mode.tools['highlight'] == True):
            if (event.x <= mode.width - 301):
                mode.currentCoords[2], mode.currentCoords[3] = event.x, event.y
            else:
                mode.currentCoords[2], mode.currentCoords[3] = mode.width-301, \
                                                                event.y
        elif (mode.tools['underline'] == True):
            if (event.x <= mode.width - 301):
                mode.currentCoords[2], mode.currentCoords[3] = event.x, \
                                                        mode.currentCoords[1]
            else:
                mode.currentCoords[2], mode.currentCoords[3] = mode.width-301, \
                                                        mode.currentCoords[1]

    def mouseReleased(mode,event):
        if (((mode.currentCoords[0] != 0) and (mode.currentCoords[1] != 0))
            and
            ((mode.currentCoords[2] != 0) and (mode.currentCoords[3] != 0))):
            if (mode.tools['highlight'] == True):
                mode.highlightCoords += [mode.currentCoords]
            elif (mode.tools['underline'] == True):
                mode.underlineCoords += [mode.currentCoords]
        mode.currentCoords = [0, 0, 0, 0]

    def mouseMoved(mode, event):
        if (mode.saveButton.isOnButton(event)):
            mode.saveButton.buttonColor = 'light blue'
        elif (not mode.saveButton.isOnButton(event)):
            mode.saveButton.buttonColor = 'white'
        
        if (mode.backButton.isOnButton(event)):
            mode.backButton.buttonColor = 'light blue'
        elif (not mode.backButton.isOnButton(event)):
            mode.backButton.buttonColor = 'white'

    def keyPressed(mode, event):
        if (mode.askName == False):
            mode.input.typing(event)
        else:
            mode.name.isTyping = True
            mode.name.typing(event)
            if (event.key == 'Space'):
                mode.name.input = mode.name.input[:-1] + '-'
            elif (event.key == 'Enter'):
                mode.name.isTyping = False
                mode.name.input = mode.name.input[:-1]
                mode.findConnections()
                WorkspaceMode.NOTES[str(Note(mode.name.input, mode.input.input,
                                    mode.highlightCoords, 
                                    mode.underlineCoords))] = mode.connections
                WorkspaceMode.NOTE_OBJECTS.add(Note(mode.name.input, 
                                    mode.input.input,
                                    mode.highlightCoords, 
                                    mode.underlineCoords))
                for note in WorkspaceMode.NOTES[str(Note(mode.name.input, 
                                            mode.input.input, 
                                            mode.highlightCoords, 
                                            mode.underlineCoords))]:
                    WorkspaceMode.NOTES[note].append(str(Note(mode.name.input, 
                                            mode.input.input, 
                                            mode.highlightCoords, 
                                            mode.underlineCoords)))
                WorkspaceMode.NOTE_TAGS[str(Note(mode.name.input, 
                                        mode.input.input,
                                        mode.highlightCoords, 
                                        mode.underlineCoords))] = []
                WorkspaceMode.NOTE_SELECTED[str(Note(mode.name.input, 
                                        mode.input.input,
                                        mode.highlightCoords, 
                                        mode.underlineCoords))] = False
                WorkspaceMode.createNoteGroups()
                mode.appStarted()
                mode.app.setActiveMode(mode.app.runWorkspaceMode)
    
    def toolChange(mode, event, button, tool):
        if (button.buttonColor != 'light blue'):
            mode.tools['highlight'] = mode.tools['underline'] = False
            mode.tools[tool] = True
            mode.highlightButton.buttonColor \
                = mode.underlineButton.buttonColor \
                = 'white'
            button.buttonColor = 'light blue'
        else:
            mode.tools[tool] = False
            button.buttonColor = 'white'

    def styleChange(mode, event, button, style):
        if (button.buttonColor != 'light blue'):
            mode.input.setStyle(style)
            mode.tools['highlight'] == mode.tools['underline'] == False
            mode.boldButton.buttonColor \
                = mode.italicizeButton.buttonColor \
                = 'white'
            button.buttonColor = 'light blue'
        else:
            button.buttonColor = 'white'
            mode.input.setStyle('normal')

    def drawCurrentHighlight(mode, canvas):
        if (((mode.currentCoords[0] != 0) and (mode.currentCoords[1] != 0))
            and
            ((mode.currentCoords[2] != 0) and (mode.currentCoords[3] != 0))):
            canvas.create_rectangle(mode.currentCoords[0], 
                                    mode.currentCoords[1], 
                                    mode.currentCoords[2], 
                                    mode.currentCoords[3], 
                                    fill='light blue', outline='lightblue')
    
    def drawCurrentUnderline(mode, canvas):
        if (((mode.currentCoords[0] != 0) and (mode.currentCoords[1] != 0))
            and
            ((mode.currentCoords[2] != 0) and (mode.currentCoords[3] != 0))):
            canvas.create_line(mode.currentCoords[0], mode.currentCoords[1], 
                                mode.currentCoords[2], mode.currentCoords[1], 
                                fill='cornflowerblue', width='3')

    def drawExistingHighlightAndUnderlines(mode, canvas):
        for startX, startY, endX, endY in mode.highlightCoords:
            canvas.create_rectangle(startX, startY, endX, endY,
                                    fill='light blue', outline='lightblue')
        for startX, startY, endX, endY in mode.underlineCoords:
            canvas.create_line(startX, startY, endX, endY,
                                fill='cornflowerblue', width='3')

    def drawInput(mode, canvas):
        mode.input.showTyping(canvas)

    def drawButtons(mode, canvas):
        mode.saveButton.makeButton(canvas)
        mode.backButton.makeButton(canvas)
        mode.boldButton.makeButton(canvas)
        mode.italicizeButton.makeButton(canvas)
        mode.highlightButton.makeButton(canvas)
        mode.underlineButton.makeButton(canvas)

    def drawAskNameBox(mode, canvas):
        canvas.create_rectangle(mode.width/2-180, mode.height/2-50,
                                mode.width/2+180, mode.height/2+50, 
                                fill='white smoke')
        canvas.create_rectangle(mode.width/2-150, mode.height/2,
                                mode.width/2+50, mode.height/2+40, 
                                fill='white')
        mode.name.drawInputPrompt(canvas)
        mode.enterNameButton.makeButton(canvas)
        mode.name.showTyping(canvas)
    
    def redrawAll(mode, canvas):
        if (WorkspaceMode.LOADING_NOTE == True):
            mode.loadedNote = WorkspaceMode.ACTIVE_NOTE
            mode.loadNote()
            WorkspaceMode.LOADING_NOTE = False

        canvas.create_rectangle(0, 0, mode.width, mode.height, 
                                fill='white smoke')
        canvas.create_rectangle(0, 0, mode.width-300, mode.height, fill='white',
                                outline='black')
        mode.drawButtons(canvas)

        if (mode.tools['highlight'] == True): 
            mode.drawCurrentHighlight(canvas)
        elif (mode.tools['underline'] == True):
            mode.drawCurrentUnderline(canvas)
        mode.drawExistingHighlightAndUnderlines(canvas)
        
        mode.drawInput(canvas)

        if (mode.askName == True):
            mode.drawAskNameBox(canvas)
        
