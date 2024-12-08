from pathlib import Path
from typing import List, Tuple, Optional

def parse_file(fp: Path) -> Tuple[List[List[str]], Tuple[int, int]]:
    grid =[]
    starting_pos = None
    with fp.open("r") as f:
        for i, line in enumerate(f.readlines()):
            char_line = []
            for j, char in enumerate(line):
                if char == '^':
                    starting_pos = (i,j)
                if char in [".", "#", "^"]:
                    char_line.append(char)
            grid.append(char_line)
    return grid, starting_pos

direction_change_grid = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

def get_next_pos_at_direction(pos: Tuple[int, int], direction: str):
    if direction == "up":
        next_pos = (pos[0] - 1, pos[1])
    elif direction == "right":
        next_pos = (pos[0], pos[1] + 1)
    elif direction == "down":
        next_pos = (pos[0] + 1, pos[1])
    else:
        next_pos = (pos[0], pos[1] - 1)

    return next_pos

def check_next_spot(grid: List[List[str]], pos: Tuple[int, int], direction: str) -> Optional[Tuple[Tuple[int, int], str]]:
    actual_next_pos = None
    potential_next_pos = get_next_pos_at_direction(pos, direction)
    if potential_next_pos[0] < 0 or potential_next_pos[0] > len(grid) -1 or potential_next_pos[1] < 0 or potential_next_pos[1] > len(grid[0]) - 1:
        # Game over, return none
        return None
    
    item_at_spot = grid[potential_next_pos[0]][potential_next_pos[1]]
    if item_at_spot in [".", "^"]:
        actual_next_pos = potential_next_pos
        new_direction = direction
    else:

        new_direction = direction_change_grid[direction]
        actual_next_pos = get_next_pos_at_direction(pos, new_direction)
        if grid[actual_next_pos[0]][actual_next_pos[1]] == "#":
            new_direction = direction_change_grid[new_direction]
            actual_next_pos = get_next_pos_at_direction(pos, new_direction)

    return (actual_next_pos, new_direction)

def partOne(fp: Path) -> List[Tuple[int, int]]:
    grid, starting_pos = parse_file(fp)
    live_pos = starting_pos
    live_direction = "up"
    visited_pos = [live_pos]
    while live_pos is not None:
        next_spot_return = check_next_spot(grid, live_pos, live_direction)
        if next_spot_return is None:
            live_pos = None
        else:
            live_pos, live_direction = next_spot_return[0], next_spot_return[1]
            if live_pos not in visited_pos:
                visited_pos.append(live_pos)
    return visited_pos


def partTwo(fp: Path) -> int:
    count = 0
    grid, starting_pos = parse_file(fp)
    visited_spots = partOne(fp)
    visited_spots.remove(starting_pos)
    for i, j in visited_spots:
        if grid[i][j] == "#":
            print(f"skipping ({i},{j})")
            continue
        
        grid[i][j] = "#"
        
        live_pos = starting_pos
        live_direction = "up"
        visited_directory = {
            live_direction: [live_pos]
        }
        while live_pos is not None:
            next_spot_return = check_next_spot(grid, live_pos, live_direction)
            
            if next_spot_return is None:
                if i == 6 and j == 77:
                    raise ValueError("something still up")
                live_pos = None
                print(f"no loop at ({i},{j})")
            else:
                live_pos, live_direction = next_spot_return[0], next_spot_return[1]
                if live_pos in visited_directory.get(live_direction, []):
                    print(f"found loop with ({i},{j})")
                    count += 1
                    live_pos = None
                dir_entry = visited_directory.get(live_direction, [])
                dir_entry.append(live_pos)
                visited_directory[live_direction] = dir_entry
        grid[i][j] = "."
    return count


fp = Path(__file__).parent / "data.txt"

print(len(partOne(fp)))
print(partTwo(fp))
