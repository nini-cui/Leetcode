#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return 0
        
        left = 0
        right = len(nums) - 1
        while left < right:
            m = left + int((right - left) / 2)

            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m
            elif nums[m] < target:
                left = m + 1
        
        return left + 1 if nums[left] < target else left
            
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.searchInsert([1, 3, 5, 6], 4)
