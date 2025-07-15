import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_KEY")

url = "https://na1.api.riotgames.com/lol/status/v4/platform-data"
headers = {
    "X-Riot-Token": RIOT_API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    incidents = data.get("incidents", [])

    if not incidents:
        print("✅ League of Legends is UP. No current issues reported.")
    else:
        print("⚠️ League of Legends is DOWN or experiencing issues.")
        print("Incidents:")
        for incident in incidents:
            print(f"- {incident.get('title', 'No title')}")
            for update in incident.get("updates", []):
                print(f"  > {update.get('content', '')}")
else:
    print("❌ Failed to check status.")
    print(f"HTTP {response.status_code}: {response.text}")
