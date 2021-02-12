import pathlib


def solution(file_path:str) -> int:
    with open(file_path, 'r') as f:
        valid_password_count = 0

        for line in f:
            # parse the input values
            first_part, second_part, input_string = line.strip().split(" ")
            min_occur, max_occur = map(int, first_part.split('-'))
            target_char = second_part[0]

            char_count = 0
            for c in input_string:
                if c == target_char:
                    char_count += 1
                    if char_count > max_occur:
                        break
            else:
                if char_count >= min_occur:
                    valid_password_count += 1

        return valid_password_count


if __name__ == "__main__":
    print(solution(f'{pathlib.Path(__file__).parent}/input.txt'))
