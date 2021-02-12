import pathlib


def solution(file_path:str) -> int:
    slope_map = []
    height = 0

    # draw map
    with open(file_path, 'r') as f:
        for line in f:
            slope_map.append(line.strip())
            height += 1

    width = len(slope_map[0])
    print(f"width, height: {width}, {height}")

    # check the tree
    tree_count = 0
    x, y = 0, 0
    while y < height-1:
        x, y = (x + 3) % width, y+1
        if slope_map[y][x] == '#':
            tree_count += 1

    return tree_count


if __name__ == "__main__":
    print(solution(f'{pathlib.Path(__file__).parent}/input.txt'))
