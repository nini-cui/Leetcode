#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)

        left = right = 1

        while right <= (nums_len - 1):
            if nums[right] != nums[left-1]:
                nums[left] = nums[right]
                right += 1
                left += 1
            elif nums[right] == nums[left-1]:
                right += 1

        return nums.index(max(nums)) + 1

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # expected result: [0, 1, 2, 3, 4]
    res = s.removeDuplicates([1, 1, 2])
    # expected result: [0, 1, 2, 3]
    # res = s.removeDuplicates([0,1,1,2,2,3])
    print(res)
