import sqlite3

class event():
    def __init__(self, eventID):
        self.id = eventID
        self.name = ''
        self.description = ''
        self.progress = ''
        self.lat = 0
        self.long = 0

    def addtoDB(self):
        eventData = sqlite3.connect('eventData.db')

        command = (f'''INSERT INTO Events (EventID) VALUES ({self.id});''')
        eventData.execute(command)
        eventData.commit()
    
    def getDescription(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Description FROM Events WHERE EventID == {self.id};''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0][0]

        self.description = output
        return output
    
    def getProgress(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Progress FROM Events WHERE EventID == {self.id};''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0][0]

        self.progress = output
        return output
    
    def removeFromDB(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''DELETE FROM Events WHERE EventID == {self.id};''')

        eventData.execute(command)
        eventData.commit()
    
    def getLatitude(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Latitude FROM Events WHERE EventID == {self.id};''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0][0]

        self.lat = output
        return output
    
    def getLongitude(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Longitude FROM Events WHERE EventID == {self.id};''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0][0]

        self.long = output
        return output