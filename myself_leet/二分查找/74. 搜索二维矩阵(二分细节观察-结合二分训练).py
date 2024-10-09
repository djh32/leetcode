from typing import List

"""
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。


"""


class Solution:

    def searchMatrix(self, matrix, target):  # 正确答案
        M, N = len(matrix), len(matrix[0])
        left, right = 0, M * N - 1
        while left <= right:
            mid = left + (right - left) // 2
            cur = matrix[mid // N][mid % N]
            if cur == target:
                return True
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix2(self, matrix, target):  # 两次二分 bisect_right 向右侧进行收缩左侧边界的方法查找col 的index
        import bisect
        M, N = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        target_row = bisect.bisect_right(col0, target) - 1
        if target_row < 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)  # 两次二分 bisect_right 向左侧进行收缩右侧边界的方法查找col 的index
        if target_col >= N:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        def bin_to_left_find(row_first_list: List[int], target) -> int:
            # 自己做的错的，但是很经典
            # 这里的二分法不能使用收缩右侧边界的方法，
            # 因为收缩右侧边界找【1，6，10】 tar=10的话会返回2，tar=8的话会返回2. 但是tar=8的时候希望返回的是1.只能使用向右侧进行收缩左侧边界的方法查找col 的index
            l, r = 0, len(row_first_list) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if row_first_list[mid] == target:
                    r = mid-1
                elif target < row_first_list[mid]:
                    r = mid - 1
                elif target > row_first_list[mid]:
                    l = mid + 1
            return r

        rows_first = [x[0] for x in matrix]
        if target in rows_first:return True

        row_check = bin_to_left_find(rows_first, target)
        if row_check < 0: return False

        row_line = matrix[row_check]
        find_idx = bin_to_left_find(row_line, target)
        if find_idx+1 > len(row_line) or row_line[find_idx+1] != target:
            return False
        else:
            return True





t = [[1, 3, 5], [6, 7, 7], [9, 10, 10], [13, 15, 17]]
print(Solution().searchMatrix(t, 12))
