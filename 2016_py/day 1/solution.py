input_path = "./input.txt"

COMPASS_POINTS = ["North", "East", "South", "West"]

def get_compass_point_idx(current: int, turn: str):
    last_direction = len(COMPASS_POINTS)-1
    
    if turn == "R":
        return current + 1 if current < last_direction else 0

    return current - 1 if current > 0 else last_direction

def choose_shortest_path(walked: list[dict[str, int]]):
    first_w = walked[0]
    last_w = walked[len(walked)-1]

    row_diff = abs( abs(first_w["row"]) - abs(last_w["row"]) )
    col_diff = abs( abs(first_w["col"]) - abs(last_w["col"]) )

    another_path_cost = col_diff + row_diff
    
    return min(last_w["cost"], another_path_cost)

def walk(path: str):
    dirs = path.split(", ")
    walked = [{ "cost": 0, "row": 0, "col": 0,}]

    current_compass_point_idx = 0

    visited = set()
    cross_section = False

    visited_twice = None

    for _, d in enumerate(dirs, 1):
        turn = d[0]
        blocks = int(d[1:])

        idx = get_compass_point_idx(current_compass_point_idx, turn)
        
        last_walked = walked[len(walked) - 1]
        w = { "cost": blocks, "row": 0, "col": 0,}

        w["cost"] += last_walked["cost"]
        w["row"] += last_walked["row"]
        w["col"] += last_walked["col"]

        visited.add((w["row"], w["col"]))

        cross_list = []
        for _ in range(0, blocks):
            # refactor: put into dict
            if COMPASS_POINTS[idx] == "North":
                w["row"] += 1
            elif COMPASS_POINTS[idx] == "East":
                w["col"] += 1
            elif COMPASS_POINTS[idx] == "South":
                w["row"] -= 1
            elif COMPASS_POINTS[idx] == "West":
                w["col"] -= 1
            
            v = (w["row"], w["col"])
            
            if v in visited:
                cross_section = True
                cross_list.append(v)
            
            if not cross_list:
                visited.add(v)

        walked.append(w)

        if cross_section and not visited_twice:
            visited_twice = True
            
            # print(cross_list)
            print("How many blocks away is the first location you visit twice? (part 2)", abs(cross_list[0][0]) + abs(cross_list[0][1]))

        current_compass_point_idx = idx

    # print("path finished")
    # print("path", walked)

    return walked

with open(input_path) as f:
    walked = walk(f.read())
    print("How many blocks away is Easter Bunny HQ? (part 1)", choose_shortest_path(walked))