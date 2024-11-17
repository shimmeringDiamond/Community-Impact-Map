import sqlite3

eventData = sqlite3.connect('eventData.db') 

try:
    eventData.execute('''CREATE TABLE Users (
            UserID VARCHAR(300) PRIMARY KEY NOT NULL,
            Name VARCHAR(40)
            ); 
            ''')

    eventData.execute(''' CREATE TABLE Events (
            EventID INTEGER PRIMARY KEY NOT NULL,
            UserID VARCHAR(300),
            Name VARCHAR(40),
            Description VARCHAR(1000),
            Progress FLOAT(5),
            Latitude FLOAT(25),
            Longitude FLOAT(25) ,
            FOREIGN KEY (UserID) REFERENCES Users(UserID));
            ''')

    eventData.commit()

except sqlite3.OperationalError:
    eventData.commit()


eventData.execute('''INSERT INTO Users (UserID, Name) VALUES
                    ('2sdihfishfifsdfu3rhi', 'Test');''')

eventData.execute('''INSERT INTO Events (Name, Description, Progress, Latitude, Longitude) VALUES
                    ('Uluru', 'Uluru, also referred to as Ayers Rock, is a large sandstone rock formation in the southern part of the Northern Territory, central Australia.', 50, -25.363, 131.044);''')

eventData.commit()
