#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_res = sorted(strs)
        first = sorted_res[0]
        last = sorted_res[-1]
        ans = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]

        return ans
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.longestCommonPrefix(["a"])
    print(res)