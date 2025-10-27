#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        max_profit = 0

        left = 0
        right = 1

        while right < prices_len:
            profit = prices[right] - prices[left]

            if profit < 0:
                left = right
                right += 1
            else:
                max_profit = max(max_profit, profit)
                right += 1
        
        return max_profit

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.maxProfit([2,1,2,1,0,1,2])
    print(res)