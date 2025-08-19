#
# @lc app=leetcode id=2933 lang=python3
#
# [2933] High-Access Employees
#
from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def convertToMins(self, t: str): 
        return 60 * int(t[:2]) + int(t[2:])

    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # res = []
        categorized_access = defaultdict(list)
        # for name, access_time in access_times:
        #     categorized_access[name].append(access_time)

        # for name, access_vals in categorized_access.items():
        #     sorted_time = sorted(access_vals)

        #     time_len = len(sorted_time)

        #     for i in range(time_len - 2):
        #         if self.convertToMins(sorted_time[i+2]) < self.convertToMins(sorted_time[i]) + 60:
        #             res.append(name)
        #             break

        for name, t in access_times:
            categorized_access[name].append(self.convertToMins(t))

        res = []

        for name, times in categorized_access.items():
            times.sort()
            left = 0

            for right in range(len(times)):
                # Shrink window while >= 60 minutes apart
                while times[right] - times[left] >= 60:
                    left += 1

                # Window size
                if right - left + 1 >= 3:
                    res.append(name)
                    break  

        return res

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    sol.findHighAccessEmployees([["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]])
