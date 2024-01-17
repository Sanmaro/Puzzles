def main():
    RED = 12
    GREEN = 13
    BLUE = 14
    games_dict = []
    power_sum = 0
    with open("2.txt") as file:
        games = [line.strip() for line in file]
        for game in games:
            games_dict.append({
                "game": int(game.split(":")[0][-2:] 
                            if games.index(game) < 99 else 100),
                "red" : max([int(round[-2:]) for round in game.split(" red")
                         if round != game.split(" red")[-1]]),
                "green" : max([int(round[-2:]) for round in game.split(" green")
                           if round != game.split(" green")[-1]]),
                "blue": max([int(round[-2:]) for round in game.split(" blue") 
                         if round != game.split(" blue")[-1]])
                })
    for game in games_dict:
        power_sum += game["red"] * game["green"] * game["blue"]
    print(power_sum)

main()
