import sqlite3

class user():
    def __init__(self, sub):
        self.name = ''
        self.id = sub
        self.eventIDs = []

    def ensure(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT COUNT(1)
                    FROM Users
                    WHERE UserID = '{self.id}';''')
        
        if eventData.execute(command) != 1:
            command = (f'''INSERT INTO Names (UserID, Name) VALUES ('{self.id}', '{self.name}');''')
            eventData.execute(command)

    def getEventIDs(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT EventID FROM Users WHERE UserID == '{self.id}';''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0]

        self.eventIDs = output
        return output
    
    def getName(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Name FROM Users WHERE UserID == '{self.id};''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0][0]

        self.name = output
        return output
    
    def linkEvent(self, eventID):
        eventData = sqlite3.connect('eventData.db')

        command = (f'''UPDATE Users
                   SET EventID = {eventID}
                    WHERE UserID == {self.id};''')
        
        eventData.execute(command)
    