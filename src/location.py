"""
location.py — Handles geolocation and editorial fallback logic

Supports location-aware phrasing, jurisdictional disclaimers, and source routing.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import os
import requests

def check_location_permission():
    """
    Checks system-level location permission.
    Returns 'granted', 'blocked', or 'undecided'.
    """
    return os.getenv("LOCATION_PERMISSION", "undecided")

def get_ip_location():
    """
    Attempts to retrieve location via IP-based lookup.
    Returns dict with city, region, country, latitude, longitude.
    """
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        loc = data.get("loc", "0,0").split(",")
        return {
            "city": data.get("city", ""),
            "region": data.get("region", ""),
            "country": data.get("country", ""),
            "latitude": float(loc[0]),
            "longitude": float(loc[1])
        }
    except Exception as e:
        return {"error": str(e)}

def get_user_location():
    """
    Returns location status and data.
    If permission is blocked or undecided, location is None.
    """
    status = check_location_permission()
    if status == "granted":
        return {"status": "granted", "location": get_ip_location()}
    elif status == "blocked":
        return {"status": "blocked", "location": None}
    else:
        return {"status": "undecided", "location": None}

def request_manual_location():
    """
    Placeholder for prompting user to specify location manually.
    In real deployment, this would trigger a UI prompt or fallback input.
    """
    return {"status": "manual", "location": {"city": "Unknown", "region": "Unknown", "country": "Unknown"}}

def resolve_location(config=None):
    """
    Resolves usable location for editorial routing.
    Falls back to manual request if permission is blocked or undecided.
    """
    user_loc = get_user_location()
    if user_loc["location"]:
        return user_loc["location"]
    elif should_prompt_for_location(config):
        return request_manual_location()["location"]
    else:
        return None

def should_prompt_for_location(config=None):
    """
    Determines whether to prompt user for manual location.
    """
    fallback = config.get("location_fallback", "ask") if config else "ask"
    return fallback == "ask"
