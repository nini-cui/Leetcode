#
# @lc app=leetcode id=1366 lang=python3
#
# [1366] Rank Teams by Votes
#
from typing import List

# @lc code=start
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # A: [5, 0, 0]
        # B: [0, 2, 3]
        # C: [0, 3, 2]

        d = {}
        vote_len = len(votes[0])
        for vote in votes:
            for i in range(vote_len):
                if vote[i] not in d:
                    d[vote[i]] = vote_len * [0]
                d[vote[i]][i] += 1
        
        voted_names = sorted(d.keys())
        res = "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))
        return res

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    sol.rankTeams(["ABC","ACB","ABC","ACB","ACB"])
