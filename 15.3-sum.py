#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# checking the current i and previous i
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = 1
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.threeSum([-2,0,1,1,2])
    print(res)
