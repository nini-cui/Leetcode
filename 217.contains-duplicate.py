#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.containsDuplicate([1,2,3])

