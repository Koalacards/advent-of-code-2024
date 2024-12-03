from pathlib import Path
import re

def get_text(fp: Path) -> str:
    return fp.read_text()


def partOne(fp: Path) -> int:
    total = 0
    text = get_text(fp)
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)
    for match in matches:
        replace = match.replace("mul(", "").replace(")","")
        splitted = replace.split(",")
        total += (int(splitted[0]) * int(splitted[1]))
    return total

def partTwo(fp: Path) -> int:
    total = 0
    text = get_text(fp)
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", text)
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            replace = match.replace("mul(", "").replace(")","")
            splitted = replace.split(",")
            total += (int(splitted[0]) * int(splitted[1]))
    return total

fp = Path(__file__).parent / "data.txt"

print(partOne(fp))
print(partTwo(fp))
