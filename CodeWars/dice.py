from collections import Counter
def score(dice):
    dice = Counter(sorted(dice))
    points = 0
    for die in dice:
        if die == 1:
            points += (dice[die] // 3 * 1000) + (dice[die] % 3 * 100)
        elif die == 5:
            points += (dice[die] // 3 * 500) + (dice[die] % 3 * 50)
        else:
            points += (dice[die] // 3 * (dice[die] * 100))
    return points

print(score( [5, 1, 3, 4, 1] ))