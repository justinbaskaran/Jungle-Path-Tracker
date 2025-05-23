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


# Process for first goal: compare spots of map pressure over time 

## Break the big problem into small problems


### 1. For a single champion , I first need to find a high level player
#### This can be broken down into smaller parts:
#### 1a. We need an API that can filter, by champion and by Rank.

##
### 2. Then I need to find a game with a similar team comp (allies and enemies), as the game I am currently playing (with similar matchups)
#### This can be broken down into smaller parts:
#### 1a. We need an API that can filter, by enemy and ally team comp


### 3. Once I have a single champion, and a game similar to his, we can dissect why the better player did the things he did.
### This can be broken up into smaller parts:
#### a. cooldowns on both enemy and allies
#### b. lane positioning
#### c. ally and enemy jungle timers.
#### d. what times they got ganked.


## Results
### We can measure success based on team gold after the first 15-20 mintues, if I have successfully implemented the strategy of the better player the gold by 15-20 difference should look similar. 


##
## Other considersations

#### 1. Teammates may have different skill levels
#### 2. Enemies may be smurfs
#### 3. Allies/eneimes may be burned out, and may make non optimal choices or not be paying as much attention



##
## Execution:
### 1. We decided on Warwick.
#### 1. One of the reasons for this is he has a very high amount of mobility, and because low elo has as lot of small fights, you need someone who can "meet" smaller fights rapidly.
#### 3. We need an api that we can use. 




