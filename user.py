import sqlite3
import math

class User():
    def __init__(self):
        self.name = ''
        self.sub = ''
        self.lat = 0
        self.long = 0
        self.eventIDs = []
        self.eventLats = []
        self.eventLongs = []

    def ensure(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT COUNT(1)
                    FROM Users
                    WHERE UserID == '{self.sub}';''')
        
        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0][0]

        if int(output) != 1:
            print("False")
            command = (f'''INSERT INTO Users (UserID, Name) 
                       VALUES ('{self.sub}, {self.name}');''')
            eventData.execute(command)
            eventData.commit()

    def getEventIDs(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT EventID FROM Events WHERE UserID == '{self.sub}';''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0]

        self.eventIDs = output
        return output
    
    def getName(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Name FROM Users WHERE UserID == '{self.sub}';''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0][0]

        self.name = output
        return output
    
    def linkEvent(self, eventID):
        eventData = sqlite3.connect('eventData.db')

        command = (f'''UPDATE Events
                   SET UserID = '{self.sub}'
                    WHERE EventID == {eventID};''')
        
        eventData.execute(command)
        eventData.commit()

    def to_dict(self):
        return {
            "sub": self.sub,
            "name": self.name,
            "lat": self.lat,
            "long": self.long
        }
    
    def __repr__(self):
        return f"User(sub={self.sub}, name={self.name})"


    