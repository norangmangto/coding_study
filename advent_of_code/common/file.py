from typing import Generator


def get_lines_from_file(file_path: str) -> Generator:
    with open(file_path, "r") as f:
        for line in f:
            yield line
