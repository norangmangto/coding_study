import pathlib


def get_row_or_column(str_input: str, max_num: int, getting_low_char: str) -> int:
    min_num = 0

    for s in str_input:
        mid_num = int((max_num + min_num + 1) / 2)
        if s == getting_low_char:
            max_num = mid_num - 1
        else:
            min_num = mid_num

    return min_num


def get_row(str_input: str) -> int:
    return get_row_or_column(str_input, 127, "F")


def get_column(str_input: str) -> int:
    return get_row_or_column(str_input, 7, "L")


def parse_bsp(str_input: str) -> (int, int):
    return get_row(str_input[:7]), get_column(str_input[7:])


def get_seat_id(str_input: str) -> int:
    row, column = parse_bsp(str_input)
    return row * 8 + column


def solution(file_path: str) -> int:
    seat_ids = []

    # read the file
    with open(file_path, "r") as f:
        for line in f:
            seat_ids.append(get_seat_id(line))

    seat_ids.sort()
    for cur_idx in range(1, len(seat_ids)):
        if seat_ids[cur_idx] == seat_ids[cur_idx - 1] + 2:
            return seat_ids[cur_idx] - 1


if __name__ == "__main__":
    print(solution(f"{pathlib.Path(__file__).parent}/input.txt"))
