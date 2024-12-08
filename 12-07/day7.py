from pathlib import Path
from typing import List

def parse_file(fp: Path) -> List[List[int]]:
    equations = []
    with fp.open("r") as f:
        for line in f.readlines(): 
            line = line.replace("\n", "")
            line = line.replace(":", "")
            equations.append([int(x) for x in line.split()])
    return equations


def solveable(l: List[int], total: int, accum: int) -> bool:
    if l == []:
        return total == accum
    else:
        return solveable(l[1:], total, l[0] + accum) or solveable(l[1:], total, l[0] * accum)

def partOne(fp: Path):
    count = 0
    equations = parse_file(fp)
    for eq in equations:
        if solveable(eq[2:], eq[0], eq[1]):
            count += eq[0]
    return count

def solveablept2(l: List[int], total: int, accum: int) -> bool:
    if l == []:
        return total == accum
    else:
        return (
            solveablept2(l[1:], total, l[0] + accum)
            or solveablept2(l[1:], total, l[0] * accum)
            or solveablept2(l[1:], total, int(f"{accum}{l[0]}"))
        )

def partTwo(fp: Path):
    count = 0
    equations = parse_file(fp)
    for eq in equations:
        if solveablept2(eq[2:], eq[0], eq[1]):
            print(f"{eq} is solveable")
            count += eq[0]
        else:
            print(f"{eq} is not solveable")
    return count

fp = Path(__file__).parent / "data.txt"

print(partOne(fp))
print(partTwo(fp))
    