import matplotlib.pyplot as plt
from valorant_stats_analyzer import ValorantStatsAnalyzer

username = input("Enter Valorant username: ")

stats = ValorantStatsAnalyzer(
    json_path="data/sample_matches.json",
    username=username
)

# PUUID is already set in the constructor
# stats.puuid = stats.detect_puuid()  <-- REMOVE this line

stats.fetch_matches()
stats.process_stats()
winrates = stats.calculate_win_rates()

if winrates is not None:
    plt.figure(figsize=(10, 6))
    plt.bar(winrates.index, winrates.values, color='skyblue')
    plt.title(f"Win Rate by Agent for {username}")
    plt.xlabel("Agent")
    plt.ylabel("Win Rate (%)")
    plt.ylim(0, 100)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
