# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements ap
# pear twice and others appear once. 
# 
#  Find all the elements that appear twice in this array. 
# 
#  Could you do it without extra space and in O(n) runtime? 
#  
#  Example: 
#  
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
#  Related Topics Array 
#  👍 2824 👎 163


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        res = []

        for c in count:
            if count[c] == 2:
                res.append(c)
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
