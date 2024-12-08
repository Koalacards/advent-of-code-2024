from pathlib import Path
from typing import Dict, Tuple, List
from itertools import combinations

GRID_MAX = 49
def parse_file(fp: Path) -> Dict[str, List[Tuple[int, int]]]:
    antenna_positions = {}
    with fp.open("r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            for j, char in enumerate(line):
                if char != ".":
                    positions = antenna_positions.get(char, [])
                    positions.append((i, j))
                    antenna_positions[char] = positions
    return antenna_positions

def check_antinotes(l: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    n1, n2 = l[0], l[1]
    deltax, deltay = (n1[0] - n2[0]), (n1[1] - n2[1])
    anti1 = (n1[0] + deltax, n1[1] + deltay)
    anti2 = (n2[0] - deltax, n2[1] - deltay)
    print(f"antis for {n1} and {n2}: {anti1}, {anti2}")
    valid_antis = []
    for anti in [anti1, anti2]:
        antix, antiy = anti[0], anti[1]
        if antix < 0 or antix > GRID_MAX or antiy < 0 or antiy > GRID_MAX:
            continue
        else:
            valid_antis.append(anti)
    return valid_antis


def partOne(fp: Path) -> int:
    anti_directory = []
    positions = parse_file(fp)
    for pos_list in positions.values():
        if len(pos_list) < 2:
            continue
        combos = list(combinations(pos_list, 2))
        for combo in combos:
            valid_antis = check_antinotes(combo)
            print(f"combo {combo} has {len(valid_antis)} valid antis")
            for valid_anti in valid_antis:
                if valid_anti not in anti_directory:
                    anti_directory.append(valid_anti)
    return len(anti_directory)

fp = Path(__file__).parent / "data.txt"

print(partOne(fp))

