class User:
    users_db = {}  # Simulate a database with a dictionary

    def __init__(self, sub=None, name=None):
        self.sub = sub
        self.name = name
        self.lat = 0
        self.long =0 

    def ensure(self):
        """If the user does not exist, add them to the 'database'."""
        if self.sub not in User.users_db:
            User.users_db[self.sub] = {
                "name": self.name,
                "ids": []
            }

    def getEventIDs(self):
        """Return a list of event IDs associated with the user."""
        if self.sub in User.users_db:
            return User.users_db[self.sub]["ids"]
        return []

    def getName(self):
        """Get the user's name from the 'database'."""
        return User.users_db.get(self.sub, {}).get("name", "Unknown")

    def linkEvent(self, id):
        """Link an event to the user."""
        if self.sub in User.users_db:
            User.users_db[self.sub]["ids"].append(id)

    def to_dict(self):
        """Convert the User object into a JSON-serializable dictionary."""
        return {
            "sub": self.sub,
            "name": self.name,
            "lat": self.lat,
            "long": self.long
        }
    
    def __repr__(self):
        return f"User(sub={self.sub}, name={self.name})"
    
    