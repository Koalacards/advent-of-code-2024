from pathlib import Path
from typing import List

def parsedata(fp: Path) -> List[List[int]]:
    output = []
    with fp.open("r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            splitted = line.split()
            output.append([int(v) for v in splitted])
    return output


def is_safe(l: List[int]) -> bool:
    safe = True
    increasing = True
    if l[1] - l[0] < 0:
        increasing = False
    for i in range(1, len(l)):
        if increasing and (l[i] - l[i-1] < 1 or l[i] - l[i-1] > 3):
            safe = False
            break
        elif not increasing and (l[i] - l[i-1] > -1 or l[i] - l[i-1] < -3):
            safe = False
            break
    return safe


def part1(fp: Path) -> int:
    safe_count = 0
    grid = parsedata(fp)
    for row in grid:
        safe = is_safe(row)
        if safe:
            safe_count += 1
    return safe_count

def part2(fp: Path) -> int:
    safe_count = 0
    grid = parsedata(fp)
    for row in grid:
        row_options = []
        for i in range(len(row)):
            copy = row.copy()
            copy.pop(i)
            row_options.append(copy)
        row_options.append(row)
        if any([is_safe(r) for r in row_options]):
            safe_count += 1
    return safe_count


fp = Path(__file__).parent / "data.txt"

print(part1(fp))
print(part2(fp))
