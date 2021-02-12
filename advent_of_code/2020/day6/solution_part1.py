from typing import Generator


def get_group(inputs: Generator) -> Generator:
    group = dict()

    for l in inputs:
        l = l.strip()
        if l == "":
            yield group
            group = dict()
        else:
            for question in l:
                group[question] = group.get(question, 0) + 1


def solution(inputs: Generator) -> int:
    sum_of_questions = 0

    for group in get_group(inputs):
        sum_of_questions += len(group)

    return sum_of_questions


if __name__ == "__main__":
    import pathlib

    from advent-of-code.utils.file import get_lines_from_file

    lines = get_lines_from_file(f"{pathlib.Path(__file__).parent}/test_input.txt")

    print(solution(lines))
