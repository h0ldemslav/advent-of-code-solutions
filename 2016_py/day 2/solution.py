with open("input.txt") as f:
    lines = list(map(lambda l: l.strip(), f.readlines()))

padlock = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
padlock_dim = 3
start_coord = [1, 1]

dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}
code = ""

#### part two
padlock = [
    ["", "", "1", "", ""],
    ["", "2", "3", "4", ""],
    ["5", "6", "7", "8", "9"],
    ["", "A", "B", "C", ""],
    ["", "", "D", "", ""],
]
padlock_dim = 5
####

for line in lines:
    current_digit = 5

    for char in line:
        dir = dirs[char]

        new_start_row_idx = start_coord[0] + dir[0]
        new_start_col_idx = start_coord[1] + dir[1]
        
        if new_start_row_idx >= padlock_dim \
            or new_start_col_idx >= padlock_dim \
            or new_start_row_idx < 0 \
            or new_start_col_idx < 0:
                pass
        elif not padlock[new_start_row_idx][new_start_col_idx]: # part two:
             pass
        else:
             start_coord[0] += dir[0]
             start_coord[1] += dir[1]

        current_digit = padlock[start_coord[0]][start_coord[1]]
    
    code += str(current_digit)

print(code)