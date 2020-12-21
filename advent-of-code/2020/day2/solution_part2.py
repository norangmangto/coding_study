import pathlib


def solution(file_path: str) -> int:
    with open(file_path, 'r') as f:
        valid_password_count = 0

        for line in f:
            # parse the input values
            first_part, second_part, input_string = line.strip().split(" ")
            first_occur, second_occur = map(int, first_part.split('-'))
            target_char = second_part[0]

            if ((input_string[first_occur-1] == target_char and input_string[second_occur-1] != target_char) or
                    (input_string[first_occur-1] != target_char and input_string[second_occur-1] == target_char)):
                valid_password_count += 1

        return valid_password_count


if __name__ == "__main__":
    print(solution(f'{pathlib.Path(__file__).parent}/input.txt'))
