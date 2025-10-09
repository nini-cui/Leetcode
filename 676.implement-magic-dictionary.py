#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#
from typing import List
import collections
# @lc code=start
class MagicDictionary:
    """
    inputs: ["hello", "leetcode"]
    case 1: if inputs is exactly the same as ele in inputs -> false 

    consideration: order needs to be preserved 
    "hhllo" -> true: convert it to a list 
    """

    def __init__(self):
        self.dict = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            if word not in self.dict:
                self.dict[word] = list(word)
        
    def search(self, searchWord: str) -> bool:
        for _, word_lst in self.dict.items():
            search_word_lst = list(searchWord)
            if len(word_lst) != len(search_word_lst):
                return False
            
            char_comparision = [(x, y) for x, y in zip(word_lst, list(searchWord)) if x != y]
            if len(char_comparision) != 1:
                return False
            
            return True

    # def __init__(self):
    #     self.buckets = collections.defaultdict(list)

    # def buildDict(self, words):
    #     for word in words:
    #         self.buckets[len(word)].append(word)
        
    #     print(self.buckets)

    # def search(self, word):
    #     return any(sum(a!=b for a,b in zip(word, candidate)) == 1
    #                for candidate in self.buckets[len(word)])

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end
if __name__ == "__main__":
    magic_dict = MagicDictionary()
    # magic_dict.buildDict(["hello", "leetcode", "abcdefgh"])
    magic_dict.buildDict([[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]])
    magic_dict.search("hhllo")
