#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_len = len(numbers)
        for i in range(nums_len):
            target_val = target - numbers[i]
            if target_val in numbers: 
                target_val_idx = numbers.index(target_val)
                if i != target_val_idx:
                    return sorted([i+1, target_val_idx+1])
# @lc code=end
if __name__ == "__main__":
    solution = Solution() 
    res = solution.twoSum([2,7,11,15], 9)   
    print(res)
