import pathlib


def solution(file_path: str) -> int:
    num_map = {}

    with open(file_path, 'r') as f:
        for num in f:
            num = int(num)

            if num in num_map:
                return num * num_map[num]
            else:
                num_map[2020 - num] = num


if __name__ == "__main__":
    print(solution(f'{pathlib.Path(__file__).parent}/input.txt'))
