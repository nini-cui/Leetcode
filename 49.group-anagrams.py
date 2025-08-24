#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted_dict = {"aet": ["edt", "ate"]}
        # list(sorted_dict.values())
        sorted_strs = defaultdict(list)
        for str in strs:
            sorted_val = ''.join(sorted(str))
            sorted_strs[sorted_val].append(str)
        
        res = sorted_strs.values()
        return list(res)
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
