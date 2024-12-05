from pathlib import Path
from typing import List

def parse_file(fp: Path) -> List[List[str]]:
    grid =[]
    with fp.open("r") as f:
        for line in f.readlines():
            char_line = []
            for char in line:
                if char in ["X", "M", "A", "S"]:
                    char_line.append(char)
            grid.append(char_line)
    return grid


def search(grid: List[List[str]], x: int, y: int, turn: int, direction: int) -> int:
    x_max = len(grid)
    y_max = len(grid[0])
    if grid[x][y] != "XMAS"[turn]:
        return 0
    
    if turn == 3:
        return 1

    turn += 1
    
    to_count_next = []
    if x != 0 and y != 0 and (direction == 0 or direction == 1):
        to_count_next.append(search(grid, x-1, y-1, turn, 1))
    if x != 0 and (direction == 0 or direction == 2):
        to_count_next.append(search(grid, x-1, y, turn, 2))
    if x != 0 and y != y_max - 1 and (direction == 0 or direction == 3):
        to_count_next.append(search(grid, x-1, y + 1, turn, 3))
    if x != x_max - 1 and y != 0 and (direction == 0 or direction == 4):
        to_count_next.append(search(grid, x+1, y-1, turn, 4))
    if x != x_max - 1 and (direction == 0 or direction ==5):
        to_count_next.append(search(grid, x+1, y, turn, 5))
    if x != x_max - 1 and y != y_max - 1 and (direction == 0 or direction == 6):
        to_count_next.append(search(grid, x+1, y + 1, turn, 6))
    if y != 0 and (direction == 0 or direction == 7):
        to_count_next.append(search(grid, x, y - 1, turn, 7))
    if y != y_max -1 and (direction == 0 or direction == 8):
        to_count_next.append(search(grid, x, y + 1, turn, 8))
    return sum(to_count_next, start=0)


def partOne(fp: Path) -> int:
    count = 0
    grid = parse_file(fp)
    for i, grid_list in enumerate(grid):
        for j in range(len(grid_list)):
            searched = search(grid, i , j, 0, 0)
            count += searched
    return count


def searchTwo(grid: List[List[str]], x: int, y: int) -> int:
    if grid[x][y] != "A":
        return 0
    
    cond1 = (grid[x-1][y-1] in ["S", "M"] and grid[x+1][y+1] in ["S", "M"]) and grid[x+1][y+1] != grid[x-1][y-1]
    cond2 = (grid[x-1][y+1] in ["S", "M"] and grid[x+1][y-1] in ["S", "M"]) and grid[x+1][y-1] != grid[x-1][y+1]
    
    if cond1 and cond2:
        return 1
    else:
        return 0


def partTwo(fp: Path) -> list:
    count = 0
    grid = parse_file(fp)
    for i, grid_list in enumerate(grid):
        if i == len(grid) - 1 or i == 0:
            continue
        for j in range(1, len(grid_list) - 1):
            searchedTwo = searchTwo(grid, i, j)
            count += searchedTwo
    return count

fp = Path(__file__).parent / "data.txt"

print(partOne(fp))
print(partTwo(fp))
