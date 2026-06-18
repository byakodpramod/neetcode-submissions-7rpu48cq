class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return matrix
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                result[c][r] = matrix[r][c]
        return result