from copy import deepcopy

def get_generation(cells : list[list[int]], generations : int) -> list[list[int]]:
    universe = deepcopy(cells)
    for row in universe:
        row.insert(0, 0)
        row.append(0)
    universe.insert(0, [0 for _ in range(len(cells)+2)])
    universe.append([0 for _ in range(len(cells)+2)])
    for i, row in enumerate(universe):
        for j in range(len(row)):
            neighbourhood = (universe[i-1][j-1] 
                + universe[i-1][j]
                + universe[i-1][j+1]
                + universe[i][j-1]
                + universe[i][j+1]
                + universe[i+1][j-1]
                + universe[i+1][j]
                + universe[i+1][j+1])
            if neighbourhood < 2 or neighbourhood > 3:
                cells[i-1][j-1] = 0
            elif neighbourhood == 3:
                cells[i-1][j-1] = 1
    return get_generation(cells, generations-1) if generations > 1 else cells

print(get_generation([
            [1,0,0],
            [0,1,1],
            [1,1,0]
        ], 1))