# from collections import defaultdict

# def tally(rows):
#     splitted = [row.split(";") for row in rows]
#     results = []
#     for i, derby in enumerate(splitted):
#         results.append({"name": derby[0]})
#         results[i] = defaultdict(lambda: 0, results[i])
#         results.append({"name": derby[1]})
#         results[i+1] = defaultdict(lambda: 0, results[i+1])
#         match derby[2]:
#             case "win":
#                 results[i]["won"] += 1
#                 results[i+1]["lost"] += 1
#             case "loss":
#                 results[i]["lost"] += 1
#                 results[i+1]["won"] += 1
#             case "draw":
#                 results[i]["tied"] += 1
#                 results[i+1]["tied"] += 1
#     print("Team                           | MP |  W |  D |  L |  P")
#     if rows:
#         for team in results:
#             print(f'{team["name"]}             '
#                   f'|  {team["won"] + team["lost"] + team["tied"]} '
#                   f'|  {team["won"]} '
#                   f'|  {team["tied"]} '
#                   f'|  {team["lost"]} '
#                   f'|  {team["won"] * 3 + team["tied"]}')


def tally(rows):
    # Splitting the rows into individual elements
    splitted = [row.split(";") for row in rows]

    # Creating a dictionary to store team statistics
    team_stats = {}
    
    for derby in splitted:
        team1, team2, result = derby
        team_stats.setdefault(team1, {"won": 0, "lost": 0, "tied": 0})
        team_stats.setdefault(team2, {"won": 0, "lost": 0, "tied": 0})

        if result == "win":
            team_stats[team1]["won"] += 1
            team_stats[team2]["lost"] += 1
        elif result == "loss":
            team_stats[team1]["lost"] += 1
            team_stats[team2]["won"] += 1
        else:
            team_stats[team1]["tied"] += 1
            team_stats[team2]["tied"] += 1

    # Creating a list of unique teams with their statistics
    results = [{"name": team, **stats} for team, stats in team_stats.items()]

    # Sorting the results based on the number of wins in descending order
    results.sort(key=lambda x: x["won"], reverse=True)

    # Creating the table
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for team in results:
        table.append(f'{team["name"]}             '
                     f'|  {team["won"] + team["lost"] + team["tied"]} '
                     f'|  {team["won"]} '
                     f'|  {team["tied"]} '
                     f'|  {team["lost"]} '
                     f'|  {team["won"] * 3 + team["tied"]}')
    
    return table


print(tally([
            "Allegoric Alaskans;Blithering Badgers;win",
            "Allegoric Alaskans;Blithering Badgers;win",
        ]))