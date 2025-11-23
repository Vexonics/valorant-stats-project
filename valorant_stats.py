import json
import pandas as pd
import os

with open("/Users/adomboateng/valorant-stats-project/data/sample_matches.json") as f:
    data = json.load(f)

username = input("Enter your Valorant username (e.g., Xen): ")
puuid = "SAMPLE_PUUID_1234567890"  

with open("data/sample_matches.json") as f:
    data = json.load(f)

matches = data["data"]
print(f"Loaded {len(matches)} sample matches.")


agent_stats = []

for match in matches:
    for player in match["players"]["all_players"]:
        if player["puuid"] == puuid:
            agent = player["character"]
            won = player["stats"]["win"]
            agent_stats.append([agent, won])
            break


df = pd.DataFrame(agent_stats, columns=["Agent", "Win"])
print("\nSample match data:")
print(df.head())

win_rates = df.groupby("Agent")["Win"].mean() * 100
print("\nWin rate by agent:\n", win_rates)

os.makedirs("data", exist_ok=True)  

df.to_csv("data/valorant_agent_stats.csv", index=False)
win_rates.to_csv("data/agent_win_rates.csv")
print("\nCSV files saved in 'data/' folder.")
