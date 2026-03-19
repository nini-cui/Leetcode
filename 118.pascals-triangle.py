#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows-1)

        cur = [1] * numRows

        for i in range(1, numRows-1):
            cur[i] = prev[-1][i-1] + prev[-1][i]

        prev.append(cur)

        return prev

        # if numRows == 1:
        #     return [[1]]
        
        # res = [[1], [1, 1]]
        # for _ in range(numRows-2):
        #     prev = res[-1]
        #     cur = []
        #     cur.append(1)
        #     for k in range(len(prev)-1):
        #         cur.append(prev[k] + prev[k+1])
        #     cur.append(1)

        #     res.append(cur)

        # return res

        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.generate(5)

