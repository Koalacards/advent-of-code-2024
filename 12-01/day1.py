from pathlib import Path

def get_lists(fp: Path) -> tuple:
    list1, list2 = [], []
    with fp.open("r") as f:
        for line in f.readlines():
            line = line.replace("\n", '')
            splitted = line.split()
            list1.append(int(splitted[0]))
            list2.append(int(splitted[1]))
    return (list1, list2)


def part1() -> int:
    lists = get_lists(Path(__file__).parent / "data.txt")
    sorted1, sorted2 = sorted(lists[0]), sorted(lists[1])
    distance = 0
    for v1, v2 in zip(sorted1, sorted2):
        distance += abs(v1 - v2)
    return distance


def part2() -> int:
    lists = get_lists(Path(__file__).parent / "data.txt")
    counts = {}
    for v in lists[1]:
        counts[v]= counts.get(v, 0) + 1
    similarity_score = 0
    for v in lists[0]:
        similarity_score += (v * counts.get(v, 0))

    return similarity_score

print(part1())
print(part2())
