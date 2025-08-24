#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# Counter()
from collections import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for cr in s:
        #     if cr not in res_s:
        #         res_s[cr] = 0
        #     res_s[cr] += 1

        # for cr in t:
        #     if cr not in res_t:
        #         res_t[cr] = 0
        #     res_t[cr] += 1

        # if len(res_s.keys()) != len(res_t.keys()):
        #     return False
            
        # for key, val in res_t.items():
        #     if key not in res_s:
        #         return False
        #     elif key in res_s:
        #         if val != res_s[key]:
        #             return False
        
        # return True

        s_count = {}
        t_count = {}
        if len(s) != len(t):
            return False
        
        s_len = len(s)
        for i in range(s_len):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        res = s_count == t_count
        print(res)
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.isAnagram("anagram", "nagaram")
