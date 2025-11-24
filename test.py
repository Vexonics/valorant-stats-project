from valorant_stats_analyzer import ValorantStatsAnalyzer

username = input("Enter your Valorant Username: ")

stats = ValorantStatsAnalyzer(
    json_path="data/sample_matches.json",
    username=username)

stats.fetch_matches()
stats.process_stats()
result = stats.calculate_win_rates()

print (result)
stats.save_csv()
