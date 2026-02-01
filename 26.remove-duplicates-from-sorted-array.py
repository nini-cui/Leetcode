#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1] = nums[right]
                left += 1

        return left + 1

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # expected result: [0, 1, 2, 3, 4]
    res = s.removeDuplicates([1,1,2])
    # res = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    # expected result: [0, 1, 2, 3]
    # res = s.removeDuplicates([0,1,1,2,2,3])
    print(res)
