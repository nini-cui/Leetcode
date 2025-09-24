#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
from collections import Counter

# count_vals.items()
# sorted() needs to pass function
# [(a, b), (c, d)] iteration
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_vals = Counter(nums)
        sorted_vals = sorted(count_vals.items(), key=lambda item: item[1], reverse=True)
        return [num for num, freq in sorted_vals[:2]]

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.topKFrequent([4,4,4,1,1,1,2,2,3], 2)
