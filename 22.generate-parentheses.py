#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

        # using stack
        # stack =  [('', n, n)]
        # res = []
        # while stack:
        #     cur = stack.pop()
        #     first_ele = cur[0]
        #     open_count = cur[1]
        #     close_count = cur[2]

        #     if open_count != 0:
        #         stack.append((first_ele + '(', open_count - 1, close_count))

        #     if close_count > open_count and close_count != 0:
        #         stack.append((first_ele + ')', open_count, close_count - 1))

        #     if open_count == close_count == 0:
        #         res.append(first_ele)
        
        # return res

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)