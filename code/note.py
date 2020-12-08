#################################################
# note.py
# this is the note object to store and load each note created
#
# Your name: Joyce Truong
# Your andrew id: btruong
# Section: C1
#################################################

# From CMU 112 Animation Part 1 Notes: 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
from cmu_112_graphics import *

class Note(object):
    def __init__(self, name, writing, highlights, underlines):
        self.name = name
        self.input = writing
        self.highlights = highlights
        self.underlines = underlines
    
    def __repr__(self):
        return self.name