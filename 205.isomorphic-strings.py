#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
from collections import defaultdict
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i

            if t[i] not in char_index_t:
                char_index_t[t[i]] = i
            
            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        return True
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.isIsomorphic("f11", "b23")
