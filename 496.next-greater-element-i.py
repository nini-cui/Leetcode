#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        mapping = {}

        # initialize stack and mapping dict
        # if nums2:
        #     stack.append(nums2[-1])

        nums2_len = len(nums2)
        for i in range(nums2_len-1, -1, -1):
            cur = nums2[i]
            while stack and cur >= stack[-1]:
                stack.pop()

            mapping[cur] = stack[-1] if stack else -1

            stack.append(cur)
        # for i in range(nums2_len-2, -1, -1):
        #     cur = nums2[i]
        #     while stack and cur >= stack[-1]:
        #         top = stack.pop()

        #     if top and top not in mapping:  
        #         mapping[top] = -1
            
        #     if stack and cur < stack[-1]:
        #         mapping[cur] = stack[-1]

        #     stack.append(cur)

        # use map to get the val

        for val in nums1:
            res.append(mapping[val])

        return res

        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # res = s.nextGreaterElement([4,1,2], [2, 1, 2, 4, 3])
    res = s.nextGreaterElement([4,1,2], [1,3,4,2])
    # res = s.nextGreaterElement([4,1,2], [1, 2, 3, 4, 5, 6])
    # res = s.nextGreaterElement([4,1,2], [6, 5, 4, 3, 2, 1])
    print(res)
