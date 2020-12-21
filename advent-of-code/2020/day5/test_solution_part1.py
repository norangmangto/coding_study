import pytest

from solution_part1 import get_row, get_column, parse_bsp, get_seat_id

get_row_test_data = [("FBFBBFF", 44)]


@pytest.mark.parametrize("input_param, expected", get_row_test_data)
def test_get_row(input_param: str, expected: int) -> None:
    assert get_row(input_param) == expected


get_column_test_data = [("RLR", 5)]


@pytest.mark.parametrize("input_param, expected", get_column_test_data)
def test_get_column(input_param: str, expected: int) -> None:
    assert get_column(input_param) == expected


parse_bsp_test_data = [
    ("BFFFBBFRRR", (70, 7)),
    ("FFFBBBFRRR", (14, 7)),
    ("BBFFBBFRLL", (102, 4)),
]


@pytest.mark.parametrize("input_param, expected", parse_bsp_test_data)
def test_parse_bsp(input_param: str, expected: int) -> None:
    assert parse_bsp(input_param) == expected


get_seat_id_test_data = [("BFFFBBFRRR", 567), ("FFFBBBFRRR", 119), ("BBFFBBFRLL", 820)]


@pytest.mark.parametrize("input_param, expected", get_seat_id_test_data)
def test_get_seat_id(input_param: str, expected: int) -> None:
    assert get_seat_id(input_param) == expected
