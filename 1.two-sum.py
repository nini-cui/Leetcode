#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum using python
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.twoSum([2,7,11,15], 9)
