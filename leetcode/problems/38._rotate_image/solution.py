class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        n_matrix = []

        n_row = []
        for y in range(n):
            for x in range(n-1, -1, -1):
                n_row.append(matrix[x][y])
            n_matrix.append(n_row)
            n_row = []

        matrix[:] = n_matrix[:]

    def other_solution(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
