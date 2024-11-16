"""Python Flask WebApp Auth0 integration example
"""

import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

from user import User
from event import Event

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")
google_api_key=env.get("GOOGLE_MAPS_API_KEY")


oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

@app.route("/scripts/map.js")
def custom_script():
    google_api_key = google_api_key
    return render_template("custom_script.js", google_api_key=google_api_key), 200, {"Content-Type": "application/javascript"}

@app.route("/add_event", methods=["POST"])
def add_event():
    # Extract data from the form
    event_data = request.json  # Use `request.form` if sending data as form-data
    description = event_data.get("description")
    progress = event_data.get("progress")
    latitude = event_data.get("latitude")
    longitude = event_data.get("longitude")
    user_sub = event_data.get("user_sub")

    # Create and save the new event
    new_event = Event()
    new_event.description = description
    new_event.progress = progress
    new_event.latitude = latitude
    new_event.longitude = longitude
    new_event.addToDb()    #should be setting id 

    user = User()
    user.sub = user_sub
    #user.ensure()  # Ensure the user exists in the database
    user.linkEvent(new_event.id)  # Link the new event to the user

    # Return a success response
    return jsonify({"message": "Event added successfully!"}), 200

# Controllers API
@app.route("/")
def home():
    # check if user exists in db, add to db if not
    
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("userinfo"), indent=4), #This is the user information
        google_api_key=google_api_key
    )

@app.route("/map")
def map():
    user = User()
    session_user = session.get("user")
    user.name = session_user.get("userinfo", {}).get("name")
    user.sub = session_user.get("userinfo", {}).get("sid")
    user.lat = 53.3806457 
    user.long = -1.466667
    user.ensure()

    # Get events for user
    eventIDs = user.getEventIDs()
    userEvents = []
    for ID in eventIDs:
        event = Event()
        event.id = ID
        event.getDescription()
        event.getProgress()
        event.getLatitude()
        event.getLongitude()
        userEvents.append(event)
    
    nearEvents = Event.getEvents(user.lat, user.long)

    events = userEvents + nearEvents

    return render_template(
        "map.html",
        google_api_key=google_api_key,
        events=userEvents,
        user=user,
        userEvents=userEvents
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))
