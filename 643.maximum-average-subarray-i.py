#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
from typing import List
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k
    
        # nums_len = len(nums)

        # if k == 1:
        #     return max(nums)
        
        # if nums_len <= k:
        #     return sum(nums) / k
        
        # left = 0
        # right = k - 1 
        # max_sum = float('-inf')
        
        # while right < nums_len:
        #     if left == 0:
        #         initial_sum = sum(nums[left:right+1])
        #         cur_sum = initial_sum
        #     else:
        #         cur_sum = cur_sum - nums[left-1] + nums[right]

        #     max_sum = max(max_sum, cur_sum)

        #     left += 1
        #     right += 1

        # return max_sum / k
       
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.findMaxAverage([1,12,-5,-6,50,3], 4)
    print(res)
