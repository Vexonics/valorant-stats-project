import requests
import pandas as pd

username = input("Type in your Valorant username (eg., Vexonics): ")
tagline = input ("Enter your Valorant tagline(eg., NA1): ")
region = input("Enter your region (na/eu/ap/kr): ").lower()
url = f"https://api.henrikdev.xyz/valorant/v1/matches/{region}/{username}/{tagline}"

Oresponse = requests.get(url)

if response.status_code != 200:
    print ("Error fetcheing datat. Check username/tag.")
    exit()

data = response.json()

matches = data["data"]
agent_stats = []

for match in matches:
    player = match["players"]["all_players"]
    
    for p in player:
        if p["name"].lower() == username.lower():
            agent = p["character"]
            won = match["teams"][p["team"]["won"]]
            agent_stats.append([agent, won])

df = pd.DataFrame(agent_stats, columns=["Agent","Win"])
print (df.head())

win_rates = df.groupby("Agent")["Win"].mean()*100
print("\nWinrate by agent:\n", win_rates)
