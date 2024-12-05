from pathlib import Path
from typing import List
import math

rules_dict = {}

def parsedata(fp: Path) -> List[List[str]]:
    sequences = []
    rules_stage = True
    with fp.open("r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            if line == "":
                rules_stage = False
                continue
            if rules_stage == True:
                splitted = line.split("|")
                rule_list = rules_dict.get(splitted[0], [])
                rule_list.append(splitted[1])
                rules_dict[splitted[0]] = rule_list
            else:
                sequences.append(line.split(","))
    return sequences


def correct_sequence(seq: List[str]) -> bool:
    for i, num in enumerate(seq):
        for subnum in seq[i+1:]:
            if num in rules_dict.get(subnum, []):
                return False
    return True

def make_correct_sequence(seq: List[str]) -> List[str]:
    ans = []
    numbers_remaining = seq.copy()
    while len(numbers_remaining) != 0:
        for num in seq:
            if num not in numbers_remaining:
                continue
            subseq=numbers_remaining.copy()
            subseq.remove(num)
            necessary_before = rules_dict.get(num, [])
            if frozenset(necessary_before).isdisjoint(frozenset(subseq)):
                numbers_remaining.remove(num)
                ans.append(num)
    ans.reverse()
    return ans

def partOne(fp: Path) -> int:
    total = 0
    data = parsedata(fp)
    for seq in data:
        if correct_sequence(seq):
            middle = int(seq[math.floor(len(seq) / 2)])
            total += middle
    return total

def partTwo(fp: Path) -> int:
    total = 0 
    data = parsedata(fp)
    for seq in data:
        if not correct_sequence(seq):
            new_seq = make_correct_sequence(seq)
            middle = int(new_seq[math.floor(len(new_seq) / 2)])
            total += middle
    return total

fp = Path(__file__).parent / "data.txt"

print(partOne(fp))
print(partTwo(fp))
