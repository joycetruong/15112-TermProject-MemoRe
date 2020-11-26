# button.py

class Button(object):

    def __init__(self, label, location):
        self.label = label
        self.location = location
        self.buttonColor = 'white'
        self.textColor = 'gray20'
    
    def isOnButton(self, event):
        return ((self.location[0] <= event.x <= self.location[2])
                and (self.location[1] <= event.y <= self.location[3]))
    
    def makeButton(self, canvas):
        canvas.create_rectangle(self.location[0], self.location[1],
                                self.location[2], self.location[3], 
                                fill=self.buttonColor, outline='gray20')
        canvas.create_text(self.location[0]+ 
                            (self.location[2]-self.location[0])/2, 
                            self.location[1]+ 
                            (self.location[3]-self.location[1])/2, 
                            text=self.label, font='Gilroy 14', 
                            fill=self.textColor)