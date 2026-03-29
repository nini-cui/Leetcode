#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
from typing import List
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        prev = self.getRow(rowIndex-1)

        cur = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            cur[i] = prev[i-1] + prev[i]

        prev = cur
        
        return prev

        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))
