#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        for n in nums_set:
            max_len = 0
            if (n - 1) not in nums_set:
                max_len += 1
                while (n + 1) in nums_set:
                    n += 1
                    max_len += 1
            length = max(max_len, length)

        return length

        # if len(nums) <= 1:
        #     if nums:
        #         return 1
        #     else:
        #         return 0
        
        # nums = sorted(set(nums))
        
        # left = 0
        # right = 1
        # max_len = 0
        # max_len_lst = []
        # while right <= (len(nums)-1):
        #     if nums[right] - nums[left] == 1:
        #         max_len += 1
        #         if right == (len(nums)-1):
        #             if nums[right] - nums[left] == 1:
        #                 max_len_lst.append(max_len+1)
        #     else:
        #         max_len_lst.append(max_len+1)
        #         max_len = 0 

        #     left += 1
        #     right += 1
        
        # if max_len_lst:
        #     return max(max_len_lst)
        # else:
        #     return max_len+1

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # res = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
    res = s.longestConsecutive([-1, 0, 1, 3, 4, 5, 6, 7])
    print(res)
