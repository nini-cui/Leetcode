#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
from collections import Counter
# @lc code=start
class Solution:
    # method 1: get the counter of t then loop through s, deduct from counter_t
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        if len(s_counter) != len(t_counter):
            return list(set(list(t_counter.keys())) - set(list(s_counter.keys())))[0]
        
        for k, v in s_counter.items():
            if v != t_counter[k]:
                return k
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheDifference("a", "aa"))
