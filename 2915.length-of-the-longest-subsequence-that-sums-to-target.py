#
# @lc app=leetcode id=2915 lang=python3
#
# [2915] Length of the Longest Subsequence That Sums to Target
#
from typing import List
# @lc code=start
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1] and dp[i - 1][j - nums[i - 1]] != -1:
                    dp[i][j] = max(1 + dp[i - 1][j - nums[i - 1]], dp[i][j])
        
        return dp[n][target]
        
# @lc code=end
if __name__ == "__main__":
    # solution = Solution()
    # solution.lengthOfLongestSubsequence([1,2,3,4,5], 9)
    test_list = [1, 2, 3, 4, 5, 6]
    for i in range(int(len(test_list)/2)):
        temp = test_list[i]
        test_list[i] = test_list[-(i+1)]
        test_list[-(i+1)] = temp

    assert test_list == [6, 5, 4, 3, 2, 1]
        
