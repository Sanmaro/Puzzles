def dir_reduc(arr):
    start_len = len(arr)
    end_len = -1
    while start_len != end_len:
        start_len = len(arr)
        for i in range(-1, -len(arr), -1):
            try:
                if ((sorted([arr[i-1], arr[i]]) == ["NORTH", "SOUTH"])
                or ((sorted([arr[i-1], arr[i]]) == ["EAST", "WEST"]))):
                    arr.pop(i)
                    arr.pop(i)
            except IndexError:
                pass
        end_len = len(arr)
    return arr


# Different solution
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
 

# Recursive one
def dirReducRec(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReducRec(dir3) if len(dir3) < len(arr) else dir3

print(dirReducRec([
    "EAST", "EAST", "WEST", "NORTH", "WEST", 
    "EAST", "EAST", "SOUTH", "NORTH", "WEST"]))