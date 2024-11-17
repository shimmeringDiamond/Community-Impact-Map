import sqlite3
import math

class Event():
    def __init__(self):
        self.id = 0
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
    
    def to_dict(self):
        return {
            "description": self.description,
            "progress": self.progress
        }
    
    @staticmethod
    def coordsToDistance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of Earth in kilometers
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c
    
    @staticmethod
    def getAllLats(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Latitude FROM Events;''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0]

        return (output)
    
    @staticmethod
    def getAllLongs(self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT Longitude FROM Events;''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0]
        
        return (output)
    
    @staticmethod
    def getAllIDs (self):
        eventData = sqlite3.connect('eventData.db')
        command = (f'''SELECT EventID FROM Events;''')

        eventDataOutput = eventData.execute(command)
        eventData.commit()

        output = (eventDataOutput.fetchall())[0]
        
        return (output)      
    
    @staticmethod
    def getEvents(self, userLat, userLong, radius):
        nearbyEvents = []
        eventLats = Event.getAllLats()
        eventLongs = Event.getAllLongs()
        eventIDs = Event.getAllIDs()

        for i in range(eventLats):
            eventLat = eventLats[i]
            eventLong = eventLongs[i]

            distance = Event.coordsToDistance(userLat,userLong, eventLat, eventLong)

            if distance <= radius:
                eventData = sqlite3.connect('eventData.db')
                command = (f'''SELECT Description, Progress FROM Events WHERE EventID == {eventIDs[i]};''')

                eventDataOutput = eventData.execute(command)
                eventData.commit()


                output = (eventDataOutput.fetchall())
                nearbyEvents.append(Event(
                    id = eventIDs[i],
                    description = output[i][0],
                    progress = output[i][1],
                    latitude=eventLats[i],
                    longitude=eventLongs[i]
                ).to_dict())

        return nearbyEvents
# eventData = sqlite3.connect('eventData.db')
# command = (f'''SELECT Description, Progress FROM Events WHERE EventID == 1;''')

# eventDataOutput = eventData.execute(command)
# eventData.commit()

# output = (eventDataOutput.fetchall())[0][1]
# print(output)


        
    