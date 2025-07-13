class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Use the second bit to store the next state.
        """
        m = len(board)
        n = len(board[0])

        for low in range(m):
            for column in range(n):
                live_cnt = 0
                for i in range(max(low - 1, 0), min(low + 2, m)):
                    for j in range(max(column - 1, 0), min(column + 2, n)):
                        live_cnt += board[i][j] & 1

                if live_cnt == 3 or live_cnt - board[low][column] == 3:
                    board[low][column] |= 2

        for low in range(m):
            for column in range(n):
                board[low][column] >>= 1
    # O(mn) time complexity, O(1) space complexity

    def other_solution(self, board: list[list[int]]) -> None:
        """
        Use addtional space to store the next state.
        """
        m = len(board)
        n = len(board[0])
        next_state = [[0] * n for _ in range(m)]

        for low in range(m):
            for column in range(n):
                live_cnt = 0
                for i in range(max(low - 1, 0), min(low + 2, m)):
                    for j in range(max(column - 1, 0), min(column + 2, n)):
                        live_cnt += board[i][j]

                if live_cnt == 3 or live_cnt - board[low][column] == 3:
                    next_state[low][column] = 1

        for low in range(m):
            for column in range(n):
                board[low][column] = next_state[low][column]
    # O(mn) time complexity, O(mn) space complexity
