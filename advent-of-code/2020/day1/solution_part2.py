import pathlib


def solution() -> int:
    one_number_list = []
    two_number_map = {}

    with open(f'{pathlib.Path(__file__).parent}/input.txt', 'r') as input:
        for num in input:
            num = int(num)

            if num in two_number_map:
                return num * two_number_map[num]
            else:
                for i in one_number_list:
                    two_number_map[2020 - num - i] = num * i

                one_number_list.append(num)


if __name__ == "__main__":
    print(solution())