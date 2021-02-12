from typing import Generator, Dict


def get_group(inputs: Generator) -> Generator:
    def _get_base_group() -> Dict:
        return {"people": 0, "questions": dict()}

    group = _get_base_group()

    for one_input in inputs:
        one_input = one_input.strip()
        if one_input == "":
            yield group
            group = _get_base_group()
        else:
            group["people"] += 1
            for question in one_input:
                group["questions"][question] = group["questions"].get(question, 0) + 1
    else:
        yield group


def solution(inputs: Generator) -> int:
    sum_of_questions = 0

    for group in get_group(inputs):
        sum_of_questions += len(group["questions"])

    return sum_of_questions


if __name__ == "__main__":
    import sys
    import os
    import pathlib

    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

    from common.file import get_lines_from_file

    lines = get_lines_from_file(f"{pathlib.Path(__file__).parent}/input.txt")

    print(solution(lines))
