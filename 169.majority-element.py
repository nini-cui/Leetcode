#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[int(len(nums/2))]
    
        # res_dict = defaultdict(int)
        # max_val, res = 0, 0
        # for num in nums:
        #     res_dict[num] += 1

        # for k, v in res_dict.items():
        #     if v > max_val:
        #         max_val = v
        #         res = k

        # return res
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.majorityElement([2,2,1,1,1,2,2])
