class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mLen = len(matrix) - 1
        nLen = len(matrix[0]) - 1

        if target < matrix[0][0] or target > matrix[mLen][nLen]:
            return False

        for i in range(len(matrix)):
            if target > matrix[i][nLen]:
                continue
            else:
                r = nLen
                l = 0

                while l <= r:
                    m = (r + l) // 2

                    if matrix[i][m] < target:
                        l = m + 1
                    elif matrix[i][m] > target:
                        r = m - 1
                    else:
                        return True
        return False