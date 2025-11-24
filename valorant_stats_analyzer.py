import json
import pandas as pd
import random

class ValorantStatsAnalyzer:
    def __init__(self, username, json_path):
        self.username = username
        self.puuid = "SAMPLE_PUUID"   # using fake PUUID
        self.json_path = json_path
        self.matches = []
        self.agent_stats = pd.DataFrame()

    def fetch_matches(self):
        with open(self.json_path) as f:
            data = json.load(f)
        self.matches = data.get("data", [])

    def process_stats(self):
        stats = []
        for match in self.matches:
            players = match["players"]["all_players"]
            for p in players:
                if p["puuid"].lower() == self.puuid.lower():
                    agent = p["character"]
                    won = random.uniform(0,1)
                    stats.append([agent, won])
        self.agent_stats = pd.DataFrame(stats, columns=["Agent", "Win"])

    def calculate_win_rates(self):
        if self.agent_stats.empty:
            print("No stats to calculate.")
            return None
        return self.agent_stats.groupby("Agent")["Win"].mean() * 100

    def save_csv(self):
        self.agent_stats.to_csv("data/agent_match_details.csv", index=False)
        print("Saved: data/agent_match_details.csv")
