import requests
import json
from datetime import timedelta
import matplotlib.pyplot as plt

API_KEY = ""

RIOT_ID = "HardstuckBronzey"
TAGLINE = "BRNZE"  # Example: "NA1"

def get_puuid(riot_id, tagline):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tagline}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("puuid")


def get_match_history(puuid, count=5):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()  # Returns a list of match IDs




def get_match_timeline(match_id):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={API_KEY}"
    response = requests.get(url)
    return response.json()  # Returns the match timeline

def extract_jungle_camps(timeline_data, player_id, time_limit=600000):
    jungle_events = []
    print(timeline_data)
    # Iterate through timeline frames (each frame represents a snapshot in the match)
    for frame in timeline_data["info"]["frames"]:
        for event in frame["events"]:
            if event["type"] == "CHAMPION_KILL":
                jungle_events.append({
                    "timestamp": event["timestamp"] // 1000,  # Convert ms → sec
                    "position": event["position"]
                })

    return jungle_events

def format_jungle_path(jungle_path):
    formatted = []
    for event in jungle_path:
        time_str = str(timedelta(seconds=event["timestamp"]))  # Convert sec to mm:ss format
        formatted.append(f"{time_str} - ({event['position']['x']}, {event['position']['y']})")
    return "\n".join(formatted)





def visualize_jungle_path(jungle_path,jungle_path_2):
    x = [event["position"]["x"] for event in jungle_path]
    y = [event["position"]["y"] for event in jungle_path]
    labels = ["1" for event in jungle_path]

    x2 = [event["position"]["x"] for event in jungle_path_2]
    y2 = [event["position"]["y"] for event in jungle_path_2]

    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color="red", label="Jungle Camps")
    plt.scatter(x2, y2, color="blue", label="Jungle Camps")
    
    for i, label in enumerate(labels):
        plt.text(x[i], y[i], label, fontsize=10, ha='right')
        plt.text(x2[i], y2[i], label, fontsize=10, ha='right')

    plt.xlabel("Map X Coordinate")
    plt.ylabel("Map Y Coordinate")
    plt.title("Jungle Pathing")
    plt.legend()
    plt.show()


PUUID = str(get_puuid(RIOT_ID, TAGLINE))
match_ids = get_match_history(PUUID)

match_timeline = get_match_timeline('NA1_5242369124')
match2_timeline = get_match_timeline('NA1_5243023447')

player_id = 2  # The player’s in-game participant ID
jungle_path = extract_jungle_camps(match_timeline, player_id)
jungle_path_2 = extract_jungle_camps(match2_timeline, player_id)



visualize_jungle_path(jungle_path,jungle_path_2)
