import math
class Event:
    events_db = {}  # Simulate a database with a dictionary
    event_counter = 1  # To generate unique event IDs

    def __init__(self, id=None, description=None, progress=None, latitude=None, longitude=None):
        self.id = id or Event.event_counter
        self.description = description
        self.progress = progress
        self.latitude = latitude
        self.longitude = longitude

        if id is None:
            Event.event_counter += 1

    def addToDb(self):
        """Add the event to the 'database'."""
        Event.events_db[self.id] = {
            "description": self.description,
            "progress": self.progress,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def getDescription(self):
        """Retrieve the event description from the 'database'."""
        return Event.events_db.get(self.id, {}).get("description", "No description")

    def getProgress(self):
        """Retrieve the event progress from the 'database'."""
        return Event.events_db.get(self.id, {}).get("progress", "No progress")

    def getLatitude(self):
        """Retrieve the event latitude from the 'database'."""
        return Event.events_db.get(self.id, {}).get("latitude", 0)

    def getLongitude(self):
        """Retrieve the event longitude from the 'database'."""
        return Event.events_db.get(self.id, {}).get("longitude", 0)

    def removeFromDb(self):
        """Remove the event from the 'database'."""
        if self.id in Event.events_db:
            del Event.events_db[self.id]

    def __repr__(self):
        return f"Event(id={self.id}, description={self.description}, progress={self.progress})"
    
    def to_dict(self):
        """Convert the event object into a JSON-serializable dictionary."""
        return {
            "description": self.description,
            "progress": self.progress,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
    
    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):
        """Calculate the great-circle distance between two points on Earth in kilometers."""
        R = 6371  # Radius of Earth in kilometers
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    @staticmethod
    def getEvents(lat, lon, radius=10):
        """
        Retrieve all events within a given radius (in kilometers) from a specified latitude and longitude.
        """
        nearby_events = []
        for id, event_data in Event.events_db.items():
            
            event_lat = event_data["latitude"]
            event_lon = event_data["longitude"]
            distance = Event.haversine_distance(lat, lon, event_lat, event_lon)

            if distance <= radius:
                nearby_events.append(Event(
                    id=id,
                    description=event_data["description"],
                    progress=event_data["progress"],
                    latitude=event_lat,
                    longitude=event_lon
                ).to_dict())
        return nearby_events
