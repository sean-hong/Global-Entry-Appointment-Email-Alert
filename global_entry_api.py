from datetime import datetime
from requests import get

# map the location to an airport
def get_airport(location: int) -> str:
    airports = {
        5444: "EWR",
        5445: "PHL"
    }

    return airports.get(location)

# call the API
def call_api(location: int) -> dict:
    api_url = f"https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={location}&minimum=1"

    try:
        req = get(api_url)
        req_json = req.json()
    except Exception as e:
        print(e)

    return req_json.pop() if req_json else None

# parse the API
def read_api_data(location: int, data: dict) -> str:
    start_time = datetime.strptime(data["startTimestamp"], "%Y-%m-%dT%H:%M")

    return f"Appointment available at {get_airport(location)} on {start_time.strftime('%m/%d/%Y')} @ {start_time.strftime('%I:%M %p')}"
