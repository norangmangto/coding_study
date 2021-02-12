import pathlib


def solution(file_path: str) -> int:
    one_number_list = []
    two_number_map = {}

    with open(file_path, 'r') as f:
        for num in f:
            num = int(num)

            if num in two_number_map:
                return num * two_number_map[num]
            else:
                for i in one_number_list:
                    two_number_map[2020 - num - i] = num * i

                one_number_list.append(num)


if __name__ == "__main__":
    print(solution(f'{pathlib.Path(__file__).parent}/input.txt'))