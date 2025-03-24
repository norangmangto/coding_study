class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def _is_valid_value(v: str, num_set: set) -> bool:
            if v == "." or (1 <= int(v) <= 9 and v not in num_set):
                return True
            else:
                return False

        def _check_rows(board: list[list[str]]) -> bool:
            for row in range(9):
                num_set = set()
                for column in range(9):
                    v = board[row][column]
                    if _is_valid_value(v, num_set):
                        num_set.add(v)
                    else:
                        return False

            return True

        def _check_columns(board: list[list[str]]) -> bool:
            for column in range(9):
                num_set = set()
                for row in range(9):
                    v = board[row][column]
                    if _is_valid_value(v, num_set):
                        num_set.add(v)
                    else:
                        return False

            return True

        def _check_sub_boxes(board: list[list[str]]) -> bool:
            for row_start in [0, 3, 6]:
                for column_start in [0, 3, 6]:
                    num_set = set()
                    for row in range(row_start, row_start + 3):
                        for column in range(column_start, column_start + 3):
                            v = board[row][column]
                            if _is_valid_value(v, num_set):
                                num_set.add(v)
                            else:
                                return False

            return True

        return all([_check_rows(board), _check_columns(board), _check_sub_boxes(board)])

    def optimal_solution(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                v = board[row][column]
                if v == ".":
                    continue

                sub_box_index = (row // 3) * 3 + column // 3

                if (
                    v in rows[row]
                    or v in columns[column]
                    or v in sub_boxes[sub_box_index]
                ):
                    return False

                rows[row].add(v)
                columns[column].add(v)
                sub_boxes[sub_box_index].add(v)

        return True
