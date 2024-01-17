#  Rock, Paper, Scissors
def main():
    rock, paper, scissors = 1, 2, 3
    lost, draw, won = 0, 3, 6 
    points = []
    strategies_dict = []

    with open("2.txt") as file:
        strategies = [line.rstrip() for line in file]
        for strategy in strategies:
            strategies_dict.append({
                "opponent": strategy.split()[0], 
                "result": strategy.split()[1]
                })
            
    for strategy in strategies_dict:
        match strategy["opponent"]:
            case "A":
                if strategy["result"] == "X":
                    points.append(scissors + lost)
                elif strategy["result"] == "Y":
                    points.append(rock + draw)
                else:
                    points.append(paper + won)
            case "B":
                if strategy["result"] == "X":
                    points.append(rock + lost)
                elif strategy["result"] == "Y":
                    points.append(paper + draw)
                else:
                    points.append(scissors + won)
            case "C":
                if strategy["result"] == "X":
                        points.append(paper + lost)
                elif strategy["result"] == "Y":
                    points.append(scissors + draw)
                else:
                    points.append(rock + won)

    print(sum(points))

if __name__ == "__main__":
    main()