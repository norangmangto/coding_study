class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        x, y, dx, dy = 0, 0, 0, 1
        for _ in range(m*n):
            res.append(matrix[x][y])
            matrix[x][y] = '.'

            if (
                not 0 <= x+dx < m or
                not 0 <= y+dy < n or
                matrix[x+dx][y+dy] == '.'
            ):
                dx, dy = dy, -dx

            x += dx
            y += dy

        return res

    def optimal_solution(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
