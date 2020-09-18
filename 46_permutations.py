# Given a collection of distinct integers, return all possible permutations. 
# 
#  Example: 
# 
#  
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  
#  Related Topics Backtracking 
#  👍 4391 👎 112


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recur(path, cand):
            if not cand: res.append(path)
            for i, n in enumerate(cand):
                recur(path+[n], cand[:i] + cand[i+1:])
        recur([],nums)
        return res


# leetcode submit region end(Prohibit modification and deletion)
