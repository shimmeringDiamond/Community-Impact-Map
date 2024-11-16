import sqlite3
import math

class user():
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
            command = (f'''INSERT INTO Users (UserID) 
                       VALUES ('{self.sub}');''')
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
    
    def getLatsInRange(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Latitude FROM Events;''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0]

        for i in output:
            if abs(float(i)-self.lat) < 0.09:
                self.eventLats.append(i)

        return (self.eventLats)
        
    def getLongsInRange(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Longitude FROM Events;''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0]

        for i in output:
            if abs(float(i)-self.long) < 0.2:
                self.eventLongs.append(i)
        
        return (self.eventLongs)
    
    def linkEvent(self, eventID):
        eventData = sqlite3.connect('eventData.db')

        command = (f'''UPDATE Events
                   SET UserID = '{self.sub}'
                    WHERE EventID == {eventID};''')
        
        eventData.execute(command)
        eventData.commit()


    