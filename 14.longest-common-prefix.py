#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs,key=len)
        for idx, c in enumerate(shortest):
            for str in strs:
                if str[idx] != c:
                    return shortest[:idx]
        return shortest

        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.longestCommonPrefix(["flower","flow","flight"])
    print(res)