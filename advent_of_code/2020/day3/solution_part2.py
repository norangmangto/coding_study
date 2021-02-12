import pathlib


def count_trees(slope_map: list, right: int, down: int) -> int:
    width, height = len(slope_map[0]), len(slope_map)

    # count trees
    tree_count = 0
    x, y = 0, 0
    while y < height - 1:
        x, y = (x + right) % width, y + down
        if slope_map[y][x] == '#':
            tree_count += 1

    return tree_count


def solution(file_path:str) -> int:
    slope_map = []

    # draw map
    with open(file_path, 'r') as f:
        for line in f:
            slope_map.append(line.strip())

    rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_tree_count = 1

    for rule in rules:
        total_tree_count *= count_trees(slope_map, *rule)

    return total_tree_count


if __name__ == "__main__":
    print(solution(f'{pathlib.Path(__file__).parent}/input.txt'))
