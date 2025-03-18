# League of Legends Jungle Tracker

## 📌 Overview

The League of Legends Jungle Tracker is a Python-based tool that extracts and visualizes the jungle movements from a given match. By using Riot's API, the tool retrieves jungle pathing data and plots it for analysis, helping players optimize their jungle routes.

It's main goal is compare my own jungle pathing to a professional player who plays against a similar enemy team comp. 

## ✨ Features

🔍 Fetches recent match history for a given player

📊 Formats jungle pathing data into a readable format

🎯 Visualizes jungle pathing on a scatter plot

## Requirements

Python 3.8+

Riot API Key (Get one from Riot Developer Portal)

Required Python libraries:

pip install requests matplotlib

## 🚀 Setup & Usage

🔹 1. Get Your PUUID

You need your PUUID to fetch match history. Run the script below, replacing YOUR_RIOT_API_KEY with your actual Riot API key:
```
import requests

API_KEY = "YOUR_RIOT_API_KEY"
RIOT_ID = "YourUsername"
TAGLINE = "YourTag"  # Example: "NA1"

def get_puuid(riot_id, tagline):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tagline}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("puuid")

puuid = get_puuid(RIOT_ID, TAGLINE)
print("Your PUUID:", puuid)
```
## 🔹 2. Fetch Match History

Retrieve recent match IDs using your PUUID:
```
def get_match_history(puuid, count=5):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

match_ids = get_match_history(puuid)
print(match_ids)
```
## 🔹 3. Extract Jungle Path

Use the timeline API to filter champion kills to figure out where the jungle is putting pressure 
```
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
```
## 🔹 4. Visualize Jungle Path

Plot jungle movements using Matplotlib:
```
import matplotlib.pyplot as plt

def visualize_jungle_path(jungle_path):
    x = [event["position"]["x"] for event in jungle_path]
    y = [event["position"]["y"] for event in jungle_path]
    labels = [event["monsterType"] for event in jungle_path]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color="red", label="Jungle Camps")
    
    for i, label in enumerate(labels):
        plt.text(x[i], y[i], label, fontsize=10, ha='right')

    plt.xlabel("Map X Coordinate")
    plt.ylabel("Map Y Coordinate")
    plt.title("Jungle Pathing (First 5-10 min)")
    plt.legend()
    plt.show()

visualize_jungle_path(jungle_path)
```
## 🔮 Future Enhancements

🏆 Compare jungle paths to pro players
    Three Metrics:
       
    🔍  When to get epic jungle monsters, like rift herald, void grubs, dragons
    
    🔍  When to gank top, mid, and jg (approxmiate time)
    
    🔍  When to farm, and when to get gank

📊 Aggregate data over multiple games

🤖 Build a Discord bot for real-time tracking



## 🤝 Contributing

Feel free to contribute by opening an issue or submitting a pull request!

## 📜 License

This project is licensed under the MIT License.

🚀 Optimize your jungle routes & climb the ranks!

