#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
import operator
from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators_mapping = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        s = []
        for token in tokens:
            if token in operators_mapping:
                last_operand = s.pop()
                second_last_operand = s.pop()
                cur_res = int(operators_mapping[token](int(second_last_operand), int(last_operand)))
                s.append(cur_res)
                print(f'cur_res: {cur_res}')
            else:
                s.append(token)
        
        if s:
            return int(s.pop())
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.evalRPN(["4","13","5","/","+"])
    print(res)
